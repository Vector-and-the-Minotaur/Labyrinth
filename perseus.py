import time

import anki_vector
from anki_vector.util import distance_mm, speed_mmps, degrees
from anki_vector import behavior
from anki_vector.events import Events

from nav import right_at_wall

args = anki_vector.util.parse_command_args()

with anki_vector.Robot(args.serial, enable_face_detection=True) as robot:


    def perseus(victory_flag=False, robot=robot): 
        
        if not victory_flag: 
            if victory_flag == False: 
                print('Victory Flag == False')
            if right_at_wall() == False: 
                perseus(victory_flag=False, robot=robot)
            else: 
                perseus(victory_flag=True, robot=robot)    
        if victory_flag == True: 
                print('Victory Flag == True')
perseus(victory_flag=False, robot=robot)            
            
    

