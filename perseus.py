import anki_vector
from anki_vector.util import distance_mm, speed_mmps, degrees

"""
when Vector sees an obstacle, such as a wall, have him turn right.
"""
def turn_right_at_obstacle():

    with anki_vector.Robot() as robot:


        def right_turn():
            robot.behavior.turn_in_place(degrees(-90))

        def move_straight():
            robot.behavior.drive_straight(distance_mm(300), speed_mmps(100))

        def say_hi():
            args = anki_vector.util.parse_command_args()
            with anki_vector.Robot(args.serial) as robot:
                print('Vector says hello to the minotaur')
                robot.behavior.say_text('Hello Minotaur')

        move_straight()
        right_turn()
        say_hi()

    # register obstacle (by proximity?) --> robot_observed_object
        # if within right range, set motors to turn right

if __name__ == "__main__":
    turn_right_at_obstacle()