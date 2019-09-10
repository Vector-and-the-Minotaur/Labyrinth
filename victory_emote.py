import anki_vector
import time

def victory_emote():
    with anki_vector.Robot() as robot:

        def gold_eyes():
                print("set Vector's eye color to cold")
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

if __name__ == "__main__":
    victory_emote()