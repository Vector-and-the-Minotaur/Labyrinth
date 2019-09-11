"""
trying to create recognition of custom markers in Vector
"""

import anki_vector
from anki_vector.objects import CustomObjectMarkers, CustomObjectTypes
from anki_vector.util import distance_mm, speed_mmps, degrees

def turn_right_at_obstacle():

    with anki_vector.Robot() as robot:

        def right_turn():
            robot.behavior.turn_in_place(degrees(-90))

        # TODO: only move straight till he sees a wall.

        def move_straight():
            robot.behavior.drive_straight(distance_mm(300), speed_mmps(100))

        def say_hi():
            args = anki_vector.util.parse_command_args()
            with anki_vector.Robot(args.serial) as robot:
                print('Vector says hello to the minotaur')
                robot.behavior.say_text('The babe with the power')

        right_turn()
        move_straight()
        say_hi()

def turn_left_at_obstacle():

    with anki_vector.Robot() as robot:

        def left_turn():
            robot.behavior.turn_in_place(degrees(90))

        # TODO: only move straight till he sees a wall.

        def move_straight():
            robot.behavior.drive_straight(distance_mm(300), speed_mmps(100))

        def say_hi():
            args = anki_vector.util.parse_command_args()
            with anki_vector.Robot(args.serial) as robot:
                print('Vector says hello to the minotaur')
                robot.behavior.say_text('I turned left')

        left_turn()
        move_straight()
        say_hi()

def glyph_react():

    with anki_vector.Robot(enable_custom_object_detection=True) as robot:
        wall_right_turn = robot.world.define_custom_wall(custom_object_type = CustomObjectTypes.CustomType00, 
            marker=CustomObjectMarkers.Circles2,
            width_mm=50,
            height_mm= 50.0,
            marker_width_mm=50.0,
            marker_height_mm=50.0,
            is_unique=True)

    def glyph_react_right():
        with anki_vector.Robot(enable_custom_object_detection=True) as robot:
            robot.world.define_custom_wall(custom_object_type=CustomObjectTypes.CustomType00,
                                        marker=CustomObjectMarkers.Circles2,
                                        width_mm= 50.0,
                                        height_mm= 50.0,
                                        marker_width_mm=50.0,
                                        marker_height_mm=50.0,
                                        is_unique=True)
            
            for obj in robot.world.visible_custom_objects:
                print('custom object seen with archetype: {0}'.format(obj.archetype))

            def react_to_pic():
                args = anki_vector.util.parse_command_args()
                with anki_vector.Robot(args.serial) as robot:
                    print('Vector sees the image')
                    robot.behavior.say_text('You remind me of the babe')

            react_to_pic()
            turn_right_at_obstacle()

    def glyph_react_left():
        with anki_vector.Robot(enable_custom_object_detection=True) as robot:
            robot.world.define_custom_cube(custom_object_type=CustomObjectTypes.CustomType00,
                                        marker=CustomObjectMarkers.Diamonds2,
                                        size_mm=20.0,
                                        marker_width_mm=50.0, marker_height_mm=50.0)
            
            for obj in robot.world.visible_custom_objects:
                print('custom object seen with archetype: {0}'.format(obj.archetype))

            def react_to_pic():
                args = anki_vector.util.parse_command_args()
                with anki_vector.Robot(args.serial) as robot:
                    print('Vector sees the image')
                    robot.behavior.say_text('Turning left now.')

            react_to_pic()
            turn_left_at_obstacle()
    if wall_right_turn:
        glyph_react_right()

    # glyph_react_left()

if __name__ == "__main__":
    glyph_react()