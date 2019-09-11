"""
Make Vector leave charger then drive in a square by going forward for a set distance and turning left. Repeat four times in a row. Make him go back to his docking station.
"""

import anki_vector
from anki_vector.util import degrees, distance_mm, speed_mmps

def main():
    args = anki_vector.util.parse_command_args()

    # Drive straight forward then stop and turn around.
    with anki_vector.Robot(args.serial) as robot:
        robot.behavior.drive_on_charger()
        robot.behavior.drive_off_charger()

        # loop 4 times
        for _ in range(4):
            print("Go straight.")
            robot.behavior.say_text('I go strights.')
            robot.behavior.drive_straight(distance_mm(100), speed_mmps(50))

            print("Turn right 90 degrees.")
            robot.behavior.say_text("I go rights." )
            robot.behavior.turn_in_place(degrees(-90))

        robot.behavior.drive_on_charger()
        
if __name__ == "__main__":
    main()