
"""
THIS IS OBSOLETE NOW
"""

import anki_vector
from anki_vector import behavior
from anki_vector.events import Events
from anki_vector.util import distance_mm, speed_mmps, degrees
import time
from turn_right_at_wall import right_at_wall
from victory_emote import victory_emote
said_text = False


# with anki_vector.Robot() as robot:
#     name_data_list = robot.faces.request_enrolled_names()
#     print(name_data_list.faces[3].face_id)

# conn = anki_vector.connection.Connection("Vector-A8P5", "172.16.12.102:443", "/Users/aliya/.anki_vector/Vector-A8P5-00600282.cert", "<tXsB9gznT2yRQnxo5QrGug==>", "<ControlPriorityLevel.DEFAULT_PRIORITY: 30>")

# conn.connect()

with behavior.ReserveBehaviorControl():

    with anki_vector.Robot() as robot:
        def main():

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
                        victory_emote()
                        said_text = True
                        done.set()

                    else:
                        right_at_wall()

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