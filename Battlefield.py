from Fleet import Fleet
from Herd import Herd

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.fleet.create_fleet
        self.herd.create_herd

    def display_welcome(self):
        print('Welcome to ROBOTS vs DINOSAURS!!')

    def battle(self):
        pass

    def dino_turn(self, dinosaur):
        print('Pick your dinosaur: \n(1) for {dino_one} \n(2) for {dino_two} \n(3) for {dino_three}')
        dinosaur.attack()
        

    def robo_turn(self, robot):
        print('Pick your robot: \n(1) for {robot.robo_one} \n(2) for {robo_two} \n(3) for {robo_three}')
        robot.attack()
        if self.weapon.attack_power > dinosaur.health:
            print(f'{dinosaur.name} died.')
        else:
            print(f'{dinosaur.name} was damaged. Health = {dinosaur.health}')

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        pass
        
