"""
Make Vector nod his head up and down a few times.
"""

import time, anki_vector

def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        robot.behavior.drive_off_charger()

        for _ in range(4):
            # raise head
            print("Raising head.")
            robot.motors.set_head_motor(5)
            # lower head
            print("Lowering head.")
            robot.motors.set_head_motor(-5.0)
        
        robot.behavior.drive_on_charger()
        
if __name__ == "__main__":
    main()
