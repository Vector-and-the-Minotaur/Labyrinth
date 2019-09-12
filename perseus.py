import time

import anki_vector
from anki_vector.util import distance_mm, speed_mmps, degrees
from anki_vector import behavior
from anki_vector.events import Events

from nav import face_turn, right_at_wall



def perseus(victory_flag=False): 
    
    if not victory_flag: 

        if right_at_wall() == False: 
            perseus(victory_flag=False)
        else: 
            perseus(victory_flag=True)    
        
    

