
import threading

import anki_vector
from anki_vector import behavior
from anki_vector.events import Events
from anki_vector.util import degrees
from anki_vector.util import distance_mm, speed_mmps, degrees
import time
from turn_right_at_wall import right_at_wall
from victory_emote import victory_emote

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

def main():
     def on_robot_observed_face(robot, event_type, event, done):
        print("Vector sees a face")
        global said_text
        if not said_text:
            said_text = True
            robot.behavior.say_text("I see a face!")
            done.set()

    # victory_face = False

    def on_robot_observed_face(robot, event_type, event, done):

        name_data_list = robot.faces.request_enrolled_names()
        global said_text
        if not said_text:
            if event.face_id == name_data_list.faces[3].face_id:
                robot.behavior.say_text("I see a Merry!")
                turn_left_at_obstacle()
                said_text = True
                done.set()
            
            if event.face_id == name_data_list.faces[0].face_id:
                # nonlocal victory_face
                victory_emote()
                # victory_face = True
                said_text = True
                done.set()

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

    robot.events.unsubscribe(on_robot_observed_face, Events.robot_observed_face)


if __name__ == '__main__':
    count = 0
    # nonlocal victory_face
    # while not victory_face:
    while count < 3:
        count += 1
        main()
        # time.sleep(20)