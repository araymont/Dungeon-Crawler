##
## MAIN.PY
##
## Main File, Handling main loop and setup
##
## @Date Created: Jun 17, 2025
## @Created by: Alexander Raymont
##
## ------------------------------------------------------------------------------------------------

import random
import Player
import MenuSystems
import Weapon
import Tools
import Maps


# Return over multiple lines "\x1B[2A" or "\x1B[3A" for 2 and 3 lines
# clear rest of carriage "\x1B[0K"

# In terminal it's 12 lines
# Combat grid is 8x8
# I shall try to stick to this fully

class Game():
    def Main(self):
        pass



writer = Tools.Writer_Tool("Enemy is on 13 health.")
writer.write()