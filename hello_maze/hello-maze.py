"""
small program to test our ability to connect our own code to Vector
"""
import anki_vector
import glyph_navigation as nav

def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        print('Vector says hello to the maze')
        robot.behavior.say_text('Hello Maze')

        nav.running(robot)           



if __name__ == "__main__":
    main()