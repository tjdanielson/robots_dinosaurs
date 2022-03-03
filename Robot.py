from Weapon import Weapon

class Robot:
    def __init__(self, name, weapon):
        self.name = name
        self.health = 50
        self.weapon = weapon
    
    def attack(self, dinosaur):
        print(f'{self.name} attacked {dinosaur} with {self.weapon.name}!')
        if self.weapon.attack_power > dinosaur.health:
            dinosaur.health = 0
        else:
            dinosaur.health -= self.attack_power
             
#for testing:
# robot = Robot('Test bot', Weapon('test weapon', 10))
# print(robot.name + robot.weapon.name)

# robot.attack('stego')