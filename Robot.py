from Weapon import Weapon

class Robot:
    def __init__(self, name, weapon):
        self.name = name
        self.health = 50
        self.weapon = weapon
    
    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power
        print(f'{self.name} attacked!')
        if self.attack_power > dinosaur.health:
            print(f'{dinosaur.name} died.')
        else:
            print(f'{dinosaur.name} was damaged. Health = {dinosaur.health}')
