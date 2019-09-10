import anki_vector


def victory_emote():
    with anki_vector.Robot() as robot:
        robot.anim.play_animation('anim_fistbump_requestonce_01', loop_count=2)

if __name__ == "__main__":
    victory_emote()