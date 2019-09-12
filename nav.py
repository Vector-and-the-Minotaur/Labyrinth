"""
Vector goes straight stops when he detects a wall then turns 90 degrees to the right
"""

import anki_vector
from anki_vector.util import degrees, distance_mm, speed_mmps
from victory_emote import victory_emote
from anki_vector.events import Events

import threading


said_text = False

def turn_left_at_obstacle():

    with anki_vector.Robot() as robot:

        def left_turn():
            robot.behavior.turn_in_place(degrees(90))


        def say_hi():
            args = anki_vector.util.parse_command_args()
            with anki_vector.Robot(args.serial) as robot:
                print('Vector says hello to the minotaur')
                robot.behavior.say_text('I turned left')

        say_hi()
        left_turn()

def face_observed(): 
    see_face = False
    print('in face observed')
    
    def on_robot_observed_face(robot, event_type, event, done):
        
        name_data_list = robot.faces.request_enrolled_names()
        global said_text
        if not said_text:
            see_face = False
            if event.face_id == name_data_list.faces[3].face_id:
                robot.behavior.say_text("I see a Merry!")
                turn_left_at_obstacle()
                said_text = True
                done.set()
                see_face = True
            
            if event.face_id == name_data_list.faces[0].face_id:
                # nonlocal victory_face
                victory_emote()
                # victory_face = True
                said_text = True
                done.set()
                see_face = True

    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial, enable_face_detection=True) as robot:

        # If necessary, move Vector's Head and Lift to make it easy to see his face
        robot.behavior.set_head_angle(degrees(15.0))
        robot.behavior.set_lift_height(0.0)

        done = threading.Event()
        robot.events.subscribe(on_robot_observed_face, Events.robot_observed_face, done)

        print("------ waiting for face events, press ctrl+c to exit early ------")

        try:
            if not done.wait(timeout=5):
                print("------ Vector never saw your face! ------")
        except KeyboardInterrupt:
            pass

        if see_face is True: 
            return True
        else:     
            return False

    robot.events.unsubscribe(on_robot_observed_face, Events.robot_observed_face)

def right_at_wall():
    args = anki_vector.util.parse_command_args()

    # Drive straight forward then stop and turn around.
    with anki_vector.Robot(args.serial) as robot:
        if robot.status.is_charging:
            print("Vector is currently charging.")
            robot.behavior.drive_off_charger()
            robot.behavior.say_text('Charge.')

        # found_object = robot.proximity.last_sensor_reading.found_object
        # robot.behavior.say_text('I sees a thing.')
        object_dist = robot.proximity.last_sensor_reading.distance
        stopping_distance = object_dist.distance_mm - 50.0
        print(f'Distance from object: {object_dist.distance_mm}')
        print(f'Stopping distance: {stopping_distance}')
        print("Go straight.")
        robot.behavior.say_text('I go straights.')
        robot.behavior.drive_straight(distance_mm(stopping_distance), speed_mmps(50))
        robot.motors.stop_all_motors()
        
        if face_observed() is False: 
            
            print("Turn right 90 degrees.")
            robot.behavior.say_text("I go rights." )
            print('before robot behavior turn 90')
            
            try: 
                robot.behavior.turn_in_place(degrees(-90))
            except: 
                breakpoint()   

            print('after robot behavior turn 90')
            right_at_wall()

        
    return False
       

        # robot.behavior.drive_on_charger()
        
if __name__ == "__main__":
   right_at_wall()