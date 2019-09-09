"""
trying to create recognition of custom markers in Vector
"""

import anki_vector
from anki_vector.objects import CustomObjectMarkers, CustomObjectTypes

def glyph_react():
    with anki_vector.Robot(enable_custom_object_detection=True) as robot:
        robot.world.define_custom_cube(custom_object_type=CustomObjectTypes.CustomType00,
                                    marker=CustomObjectMarkers.Circles2,
                                    size_mm=20.0,
                                    marker_width_mm=50.0, marker_height_mm=50.0)
        
        for obj in robot.world.visible_custom_objects:
            print('custom object seen with archetype: {0}'.format(obj.archetype))

        def react_to_pic():
            args = anki_vector.util.parse_command_args()
            with anki_vector.Robot(args.serial) as robot:
                print('Vector sees the image')
                robot.behavior.say_text('I see the marker. Yay Vector!')

        react_to_pic()

if __name__ == "__main__":
    glyph_react()