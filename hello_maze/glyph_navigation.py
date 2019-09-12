import anki_vector
import asyncio
from glyph import Glyph
from anki_vector.objects import CustomObjectMarkers, CustomObjectTypes
from anki_vector.util import distance_mm, speed_mmps, degrees
from anki_vector.events import Events


known_glyphs = {
  'right': Glyph(CustomObjectMarkers.Circles2, 'right', CustomObjectTypes.CustomType00),
  'left': Glyph(CustomObjectMarkers.Diamonds2, 'left', CustomObjectTypes.CustomType04), 
  'start': Glyph(CustomObjectMarkers.Triangles2, 'start', CustomObjectTypes.CustomType12), 
  'stop': Glyph(CustomObjectMarkers.Hexagons2, 'stop', CustomObjectTypes.CustomType10)
}


async def wait_for_control(conn: anki_vector.connection.Connection): 
  await conn.control_granted_event.wait()
  return True


async def auto_reconnect(conn: anki_vector.connection.Connection): 
  await conn.control_lost_event.wait() 
  conn.request_control()

def handle_object_appeared(robot, event_type, event):
    print('Vector started seeing a marker', event_type, event)
    return True

def handle_object_disappeared(robot, event_type, event):
    print('Vector stopped seeing the marker', event_type, event)
    return True

def handle_object_observed(robot, event_type, event):
  print('Vector recognized', event_type, event)
  return True

def move_straight(robot): 
  robot.behavior.drive_straight(distance_mm(50),speed_mmps(100))

def running(robot): 
  while True:
    if wait_for_control(anki_vector.connection.Connection):      
      wall = False
      while not wall: 
        move_straight(robot=robot)
        if handle_object_appeared(robot=robot, event_type=handle_object_appeared, event='object_appeared'): 
          wall= True

          if handle_object_observed(robot=robot, event_type=handle_object_observed, event='object_observed'):
            if known_glyphs['right'].seen(): 
              known_glyphs['right'].__glyph_react()

            if known_glyphs['left'].seen(): 
              known_glyphs['left'].__glyph_react()

            if known_glyphs['start'].seen(): 
              known_glyphs['start'].__glyph_react()

            if known_glyphs['stop'].seen(): 
              known_glyphs['stop'].__glyph_react()      
              
        if handle_object_disappeared(robot=robot, event_type=handle_object_disappeared, event='object_disappeared'): 
          wall = False

    else: 
      auto_reconnect(anki_vector.connection.Connection)      

if __name__ is '__main__': 
  
    args = anki_vector.util.parse_command_args()
    with anki_vector.AsyncRobot(args.serial) as robot: 
      robot.connect
      print('CLI Has Vectors Brain')

      running(robot=robot)

  

  # start(robot=robot)  
