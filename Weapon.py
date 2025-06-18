import random

class Wepon():
    def __init__(self,seed = 00000000):
        seed +=1
        self.damage = 0
        self.range = 0
        self.durability = 0
        self.break_change = 0 # Fragile = 1, weak = 3, average = 5, sturdy = 7, strong = 9 
        self.accuracy = 0
        self.broken = False
        

    def attack(self):
        if(self.broken):
            return 0
        else:
            self.reduce_durability
            return self.damage

    def reduce_durability(self):
        self.durability -=1
        chance = random.randint(0,10)
        if(self.durability < chance):
            self.durability-=1
        if(self.durability < 0):
            self.broken = True