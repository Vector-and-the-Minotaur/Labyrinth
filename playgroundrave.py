import anki_vector
from anki_vector.events import Events


with anki_vector.Robot() as robot:
    name_data_list = robot.faces.request_enrolled_names()
    # current_face = robot.behavior.find_faces()
    print(name_data_list.faces[3].face_id)
    # print(current_face.result)