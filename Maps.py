import random

class BattleRoom():
    def __init__(self):
        self.map = [["-","-","-","-","-","-","-","-"],
                    ["-","-","-","-","-","-","-","-"],
                    ["-","-","-","-","-","-","-","-"],
                    ["-","-","-","-","-","-","-","-"],
                    ["-","-","-","-","-","-","-","-"],
                    ["-","-","-","-","-","-","-","-"],
                    ["-","-","-","-","-","-","-","-"],
                    ["-","-","-","-","-","-","-","-"]]
        
    def clear_map(self):
        self.map = [["-","-","-","-","-","-","-","-"],
                    ["-","-","-","-","-","-","-","-"],
                    ["-","-","-","-","-","-","-","-"],
                    ["-","-","-","-","-","-","-","-"],
                    ["-","-","-","-","-","-","-","-"],
                    ["-","-","-","-","-","-","-","-"],
                    ["-","-","-","-","-","-","-","-"],
                    ["-","-","-","-","-","-","-","-"]]
    
    def add_to_map(self,item,x_coordinate,y_coordinate):
        self.map[7-y_coordinate][x_coordinate] = item

    def remove_from_map_coordinates(self,x,y):
        self.map[7-y][x]= "-"

    def print_map(self):
        for l in self.map:
            print(l)









class FloorMap():
    def __init__(self,level,seed = 00000000):
        seed +=2
        self.level = level
        self.rooms = [] # I think 9 rooms in 3x3, with possible enterences on each side
        self.generate_rooms()
    
    def generate_rooms(self):
        pass