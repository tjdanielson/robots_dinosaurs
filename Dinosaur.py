
class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 50
    
    def attack(self, robot):
        robot.health -= self.attack_power
        print(f'{self.name} attacked!')
        if self.attack_power > robot.health:
            print(f'{robot.name} died.')
        else:
            print(f'{robot.name} was damaged. Health = {robot.health}')
