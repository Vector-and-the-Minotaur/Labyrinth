import anki_vector
import time
from anki_vector.events import Events
from anki_vector.objects import CustomObjectMarkers, CustomObjectTypes

def victory_emote():
    with anki_vector.Robot() as robot:

        def gold_eyes():
                print("set Vector's eye color to gold")
                robot.behavior.set_eye_color(0.11, 1.00)
                time.sleep(2)

        def victory_dance():
                robot.anim.play_animation('anim_pounce_success_02', loop_count=1)

        def emote():
                robot.behavior.say_text("I won!")
        
        def green_eyes():
                print("Set Vector's eye color to green...")
                robot.behavior.set_eye_color(0.21, 1.00)
                time.sleep(10)

        gold_eyes()
        victory_dance()
        emote()
        green_eyes()

def emote_react():
        def handle_object_observed(robot, event_type, event):
                print(f"-----------Vector observed object: \n {event.obj}")

        with anki_vector.Robot(enable_custom_object_detection=True) as robot:
               
                robot.world.define_custom_cube(custom_object_type=CustomObjectTypes.CustomType14,
                marker=CustomObjectMarkers.Triangles4,
                size_mm=20.0,
                marker_width_mm=50.0,
                marker_height_mm=50.0)

                for obj in robot.world.visible_custom_objects:
                        print(f"custom object seen with archetype: {0}".format(obj.archetype))
                
                victory_emote()

if __name__ == "__main__":
        emote_react()