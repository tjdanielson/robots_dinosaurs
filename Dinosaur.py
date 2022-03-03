
class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 50
    
    def attack(self, robot):
        print(f'{self.name} attacked {robot}!')
        if self.attack_power > robot.health:
            robot.health = 0
            print(f'{self.name} landed a blow on {robot.name} dealing {self.attack_power} damage.')
        else:
            robot.health -= self.attack_power
            print(f'{self.name} attacked {robot.name} and did {self.attack_power} damage leaving {robot.name} with {robot.health} health remaining')
        

#for testing:
# dinosaur = Dinosaur('Test dino', 20)
# print(dinosaur.name + str(dinosaur.attack_power))

# dinosaur.attack('roomba')




