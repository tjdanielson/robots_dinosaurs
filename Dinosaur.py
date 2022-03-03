
class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 50
    
    def attack(self, robot):
        print(f'{self.name} attacked {robot}!')

dinosaur = Dinosaur('Test dino', 20)
print(dinosaur.name + str(dinosaur.attack_power))

dinosaur.attack('roomba')




