from Weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 0
        self.weapon = Weapon()
    
    def attack(self, dinosaur):
        pass
