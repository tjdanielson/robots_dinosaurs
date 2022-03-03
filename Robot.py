from Weapon import Weapon

class Robot:
    def __init__(self, name, weapon):
        self.name = name
        self.health = 50
        self.weapon = weapon
    
    def attack(self, dinosaur):
        if self.weapon.attack_power > dinosaur.health:
            dinosaur.health = 0
            print(f'{self.name} landed a blow on {dinosaur.name} dealing {self.weapon.attack_power} damage.')
        else:
            dinosaur.health -= self.weapon.attack_power
            print(f'{self.name} attacked {dinosaur.name} and did {self.weapon.attack_power} damage leaving {dinosaur.name} with {dinosaur.health} health remaining')
             
#for testing:
# robot = Robot('Test bot', Weapon('test weapon', 10))
# print(robot.name + robot.weapon.name)

# robot.attack('stego')