"""
Vector goes straight stops when he detects a wall then turns 90 degrees to the right
"""

import anki_vector
from anki_vector.util import degrees, distance_mm, speed_mmps

def main():
    
    args = anki_vector.util.parse_command_args()

    # Drive straight forward then stop and turn around.
    with anki_vector.Robot(args.serial) as robot:
        if robot.status.is_charging:
            print("Vector is currently charging.")
            robot.behavior.drive_off_charger()
            robot.behavior.say_text('Charge.')
        
        object_dist = robot.proximity.last_sensor_reading.distance
        print(f'Distance from object: {object_dist.distance_mm}')

        if object_dist.distance_mm == 400:
            robot.behavior.say_text('I go straights.')
            robot.behavior.drive_straight(distance_mm(400), speed_mmps(100))
            object_dist = robot.proximity.last_sensor_reading.distance
            print(f'Distance from object: {object_dist.distance_mm}')
            if object_dist.distance_mm == 400:
                robot.behavior.say_text('I am not there yet.')
                robot.behavior.drive_straight(distance_mm(400), speed_mmps(100))
                robot.motors.stop_all_motors()
                robot.behavior.say_text('I escaped the Minotaur.')
            elif object_dist.distance_mm < 400:
                robot.behavior.say_text('This is my last run.')
                robot.behavior.drive_straight(distance_mm(object_dist.distance_mm - 50), speed_mmps(100))
                print("Turn right 90 degrees.")
                robot.behavior.say_text("I go rights." )
                robot.behavior.turn_in_place(degrees(-90))
        elif object_dist.distance_mm < 400:
            stopping_distance = object_dist.distance_mm - 50.0
            print(f'Distance from object: {object_dist.distance_mm}')
            print(f'Stopping distance: {stopping_distance}')
            print("Go straight.")
            robot.behavior.say_text('I go strights.')
            robot.behavior.drive_straight(distance_mm(stopping_distance), speed_mmps(50))
            robot.motors.stop_all_motors()
            print("Turn right 90 degrees.")
            robot.behavior.say_text("I go rights." )
            robot.behavior.turn_in_place(degrees(-90))

        # robot.behavior.drive_on_charger()
        
if __name__ == "__main__":
    main()