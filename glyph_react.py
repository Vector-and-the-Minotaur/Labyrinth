import anki_vector


def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        print('Vector Provides an Introduction')
        robot.behavior.say_text('Hi! My name is Vector. Ive been working with a team of Python developers this past week. They helped me solve mazes!')
       

if __name__ == "__main__":
    main()