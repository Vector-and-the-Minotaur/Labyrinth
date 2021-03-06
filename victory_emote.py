import anki_vector
import time
from anki_vector.events import Events
from anki_vector.objects import CustomObjectMarkers, CustomObjectTypes

def victory_emote():
    with anki_vector.Robot() as robot:

        def gold_eyes():
                print("set Vector's eye color to gold")
                robot.behavior.set_eye_color(0.11, 1.00)
                time.sleep(1)

        def victory_dance():
                robot.anim.play_animation('anim_pounce_success_02', loop_count=1)

        def emote():
                robot.behavior.say_text("I see Raven! I won!")
        
        def green_eyes():
                print("Set Vector's eye color to green...")
                robot.behavior.set_eye_color(0.21, 1.00)
                time.sleep(10)

        gold_eyes()
        victory_dance()
        emote()
        green_eyes()


if __name__ == "__main__":
        victory_emote()
