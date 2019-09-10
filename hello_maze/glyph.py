import anki_vector
from anki_vector.objects import CustomObjectMarkers, CustomObjectTypes
from anki_vector.util import distance_mm, speed_mmps, degrees

class Glyph:

  def __init__(self, glyph_type, turn_direction, type_num): 
    self.glyph_type = glyph_type
    self.turn_direction = turn_direction

    with anki_vector.Robot(enable_custom_object_detection=True) as robot:
      wall_right_turn = robot.world.define_custom_wall(custom_object_type = type_num, 
        marker= glyph_type,
        width_mm=50,
        height_mm=50.0,
        marker_width_mm=50.0,
        marker_height_mm=50.0,
        is_unique=True)

      for obj in robot.world.visible_custom_objects: 
        print('custom object seen with archetype: {0}'.format(obj.archetype))

  def turn_at_obstacle(self): 
    with anki_vector.Robot() as robot: 

      if self.turn_direction == "right":
        robot.behavior.turn_in_place(degrees(-90)) 
      else: 
        robot.behavior.turn_in_place(degrees(90))  

  def __glyph_react(self):
    with anki_vector.Robot(enable_custom_object_detection=True) as robot: 
      robot.world.define_custom_wall(custom_object_type=CustomObjectTypes.CustomType00, 
                                      marker=CustomObjectMarkers.self.glyph_type, 
                                      width_mm=152.4, 
                                      height_mm=152.4,
                                      marker_width_mm=50, 
                                      marker_height_mm=50, 
                                      is_unique=False)
      for obj in robot.world.visible_custom_objects: 
        print('custom object seen with archetype: {0}'.format(obj.archetype))

    turn_at_obstacle()   



  def seen(self): 
    pass


