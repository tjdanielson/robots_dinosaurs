
class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 10
        self.energy = 50
    
    def attack(self, robot, dinosaur_attack):
        self.energy -= 10
        if self.attack_power >= robot.health:
            robot.health = 0
            print(f'{self.name} landed a blow with {dinosaur_attack}, KILLING {robot.name}.')
        else:
            robot.health -= self.attack_power
            print(f'{self.name} attacked {robot.name} with {dinosaur_attack} and did {self.attack_power} damage leaving {robot.name} with <<{robot.health} HEALTH>> remaining')
        





