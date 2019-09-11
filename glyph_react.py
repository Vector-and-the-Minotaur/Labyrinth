"""
trying to create recognition of custom markers in Vector
"""

import anki_vector
from anki_vector.objects import CustomObjectMarkers, CustomObjectTypes
from anki_vector.util import distance_mm, speed_mmps, degrees
<<<<<<< HEAD
=======
import time


'''
right turn code below
'''
>>>>>>> 49baf9eb39e9c11157de937e9346b0ed6237feee

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

<<<<<<< HEAD
=======

'''
left turn code below
'''
>>>>>>> 49baf9eb39e9c11157de937e9346b0ed6237feee
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

<<<<<<< HEAD
def glyph_react():

    with anki_vector.Robot(enable_custom_object_detection=True) as robot:
        wall_right_turn = robot.world.define_custom_wall(custom_object_type = CustomObjectTypes.CustomType00, 
            marker=CustomObjectMarkers.Circles2,
            width_mm=50,
            height_mm= 50.0,
=======
"""
Called whenever object comes into view
"""
def handle_object_appeared(robot, event_type, event):
    print('Vector started seeing a marker')

def handle_object_disappeared(robot, event_type, event):
    print('Vector stopped seeing the marker')

"""
Big main function: still need to break this down. Just trying to get functionality from recognition of custom markers
"""
def glyph_react():

    args = anki_vector.util.parse_command_args()

    def react_to_circle():
        args = anki_vector.util.parse_command_args()
        with anki_vector.Robot(args.serial) as robot:
            print('Vector sees the image')
            robot.behavior.say_text('I see circles')

    def react_to_triangle():
        args = anki_vector.util.parse_command_args()
        with anki_vector.Robot(args.serial) as robot:
            print('Vector sees the image')
            robot.behavior.say_text('I see triangles')


    with anki_vector.Robot(args.serial,
                            default_logging=False,
                            show_viewer=True,
                            show_3d_viewer=True,
                            enable_custom_object_detection=True,
                            enable_nav_map_feed=True) as robot:
        """
        Add event handling for Vector seeing a new object
        """
        robot.events.subscribe(handle_object_appeared, anki_vector.events.Events.object_appeared)
        robot.events.subscribe(handle_object_disappeared, anki_vector.events.Events.object_disappeared)

        """
        Define a unique new wall marker
        """

        wall_right_turn = robot.world.define_custom_wall(custom_object_type = CustomObjectTypes.CustomType00, 
            marker=CustomObjectMarkers.Circles2,
            width_mm=150,
            height_mm= 150.0,
            marker_width_mm=50.0,
            marker_height_mm=50.0,
            is_unique=True)
        
        wall_left_turn = robot.world.define_custom_wall(custom_object_type = CustomObjectTypes.CustomType01, 
            marker=CustomObjectMarkers.Triangles2,
            width_mm=150,
            height_mm= 150.0,
>>>>>>> 49baf9eb39e9c11157de937e9346b0ed6237feee
            marker_width_mm=50.0,
            marker_height_mm=50.0,
            is_unique=True)

<<<<<<< HEAD
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
=======
        if (wall_right_turn is not None):
            react_to_circle()
        if (wall_left_turn is not None):
            react_to_triangle()

    # def glyph_react_right():
    #     with anki_vector.Robot(enable_custom_object_detection=True) as robot:
    #         robot.world.define_custom_wall(custom_object_type=CustomObjectTypes.CustomType00,
    #                                     marker=CustomObjectMarkers.Circles2,
    #                                     width_mm= 50.0,
    #                                     height_mm= 50.0,
    #                                     marker_width_mm=50.0,
    #                                     marker_height_mm=50.0,
    #                                     is_unique=True)
            
    #         for obj in robot.world.visible_custom_objects:
    #             print('custom object seen with archetype: {0}'.format(obj.archetype))

    #         def react_to_pic():
    #             args = anki_vector.util.parse_command_args()
    #             with anki_vector.Robot(args.serial) as robot:
    #                 print('Vector sees the image')
    #                 robot.behavior.say_text('You remind me of the babe')

    #         react_to_pic()
    #         turn_right_at_obstacle()

    # def glyph_react_left():
    #     with anki_vector.Robot(enable_custom_object_detection=True) as robot:
    #         robot.world.define_custom_cube(custom_object_type=CustomObjectTypes.CustomType00,
    #                                     marker=CustomObjectMarkers.Diamonds2,
    #                                     size_mm=20.0,
    #                                     marker_width_mm=50.0, marker_height_mm=50.0)
            
    #         for obj in robot.world.visible_custom_objects:
    #             print('custom object seen with archetype: {0}'.format(obj.archetype))

    #         def react_to_pic():
    #             args = anki_vector.util.parse_command_args()
    #             with anki_vector.Robot(args.serial) as robot:
    #                 print('Vector sees the image')
    #                 robot.behavior.say_text('Turning left now.')

    #         react_to_pic()
    #         turn_left_at_obstacle()
    # if wall_right_turn:
    #     glyph_react_right()
>>>>>>> 49baf9eb39e9c11157de937e9346b0ed6237feee

    # glyph_react_left()

if __name__ == "__main__":
    glyph_react()