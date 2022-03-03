from Fleet import Fleet
from Herd import Herd

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def display_welcome(self):
        print('Welcome to ROBOTS vs DINOSAURS!!')

    def battle(self):
        pass
        

    def dino_turn(self):
        print('TEAM DINOSAUR! Pick your dinosaur: ')
        count = 1
        for i in self.herd.dinosaurs:
            if i.health > 0:
                print(f'{str(count)} for {i.name}')
                count += 1
        dinosaur_choice = input('Choose your dinosaur')
        return dinosaur_choice

        
    def robo_turn(self):
        print('TEAM ROBOT! Pick your robot: ')
        count = 1
        for i in self.fleet.robots:
            if i.health > 0:
                print(f'{str(count)} for {i.name}')
                count += 1
        robot_choice = input('Choose your robot')
        return robot_choice
    

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        pass

    def run_game(self):
        #display a welcome message
        self.display_welcome() 
        self.dino_turn()
        self.robo_turn()
        #Team dino, pick your dino for battle! (pick a dino from list --> if dino health > 0)
        #Team robot, pick your robot for battle! (pick a robot from list --> if robot health > 0)
        #if round starter variable = Dino then dino attacks robot, else robot attacks dino
        #Dino attacks robot
        #If health > 0 -- Robot attacks Dino - else: Robot is dead
        #flip round starter variable (if it was dino, now its robo)
        #Round over
        
