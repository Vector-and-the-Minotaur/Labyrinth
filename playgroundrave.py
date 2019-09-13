
import threading
import anki_vector
from anki_vector import behavior
from anki_vector.events import Events
import time
from victory_emote import victory_emote
from anki_vector.util import degrees, distance_mm, speed_mmps

said_text = False
crap_shoot = False


def turn_right_two():
    with anki_vector.Robot() as robot:

        def right_turn():
            robot.behavior.turn_in_place(degrees(225))

        right_turn()
        robot.motors.stop_all_motors()


def turn_right():
    with anki_vector.Robot() as robot:

        def right_turn():
            robot.behavior.turn_in_place(degrees(-90))

        right_turn()
        robot.motors.stop_all_motors()

def do_shit():
    args = anki_vector.util.parse_command_args()

    with anki_vector.Robot(args.serial, enable_face_detection=True) as robot:

        robot.motors.stop_all_motors()
        robot.behavior.say_text("I see a Merry!")
        robot.behavior.turn_in_place(degrees(90))


        object_dist = robot.proximity.last_sensor_reading.distance
        stopping_distance = object_dist.distance_mm - 50.0
        print(f'Distance from object: {object_dist.distance_mm}')
        print(f'Stopping distance: {stopping_distance}')
        robot.behavior.say_text('I finally did it')
        robot.behavior.drive_straight(distance_mm(stopping_distance), speed_mmps(50))

        robot.motors.stop_all_motors()

        look_for_face()

def look_for_face():

    def on_robot_observed_face(robot, event_type, event, done):
        global said_text
        name_data_list = robot.faces.request_enrolled_names()
        if not said_text:
            if event.face_id == name_data_list.faces[3].face_id:
                do_shit()
                print('turned left!!!!')
                said_text = True
                done.set()
            
            elif event.face_id == name_data_list.faces[0].face_id:
                robot.behavior.say_text("I see a Raven!")
                victory_emote()
                said_text = True
                done.set()

    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial, enable_face_detection=True) as robot:

        # If necessary, move Vector's Head and Lift to make it easy to see his face
        robot.behavior.set_head_angle(degrees(18.0))
        robot.behavior.set_lift_height(0.0)

        done = threading.Event()
        robot.events.subscribe(on_robot_observed_face, Events.robot_observed_face, done)

        print("------ waiting for face events, press ctrl+c to exit early ------")

        if not done.wait(timeout=5):
            turn_right()
            look_at_wall()
        else:
            look_at_wall()

    robot.events.unsubscribe(on_robot_observed_face, Events.robot_observed_face)


def look_at_wall():
    args = anki_vector.util.parse_command_args()

    # Drive straight forward then stop and turn around.
    with anki_vector.Robot(args.serial) as robot:
        if robot.status.is_charging:
            print("Vector is currently charging.")
            robot.behavior.drive_off_charger()
            robot.behavior.say_text('Charge.')

        object_dist = robot.proximity.last_sensor_reading.distance
        stopping_distance = object_dist.distance_mm - 50.0
        print(f'Distance from object: {object_dist.distance_mm}')
        print(f'Stopping distance: {stopping_distance}')
        print("Go straight.")
        robot.behavior.say_text('I go straights.')
        robot.behavior.drive_straight(distance_mm(stopping_distance), speed_mmps(50))

        robot.motors.stop_all_motors()

        look_for_face()
        # crap()


if __name__ == '__main__':

    look_at_wall()