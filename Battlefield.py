from Fleet import Fleet
from Herd import Herd

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def display_welcome(self):
        print('Welcome to ROBOTS vs DINOSAURS!!')

    def battle(self):
        dino_start = True
        dinasaur_choice = self.show_dino_fighter_options()
        robot_choice = self.show_robo_fighter_options()
        if dino_start == True:
            self.dino_turn(dinasaur_choice, robot_choice)
            self.robo_turn(robot_choice, dinasaur_choice)
            dino_start = False  
        else:
            self.robo_turn(robot_choice, dinasaur_choice)
            self.dino_turn(dinasaur_choice, robot_choice)
            dino_start = True

        
    def dino_turn(self, dinosaur_choice, robot_choice):
        print('Dinosaurs turn')
        dinosaur_choice.attack(robot_choice)
        

    def robo_turn(self, robot_choice, dinosaur_choice):
        print('Robots turn')
        robot_choice.attack(dinosaur_choice)
    

    def show_dino_fighter_options(self):
        print('TEAM DINOSAUR! Pick your dinosaur: ')
        count = 0
        for i in self.herd.dinosaurs:
            if i.health > 0:
                print(f'{str(count)} for {i.name}. Remaining Health: {i.health}')
                count += 1
        dinosaur_choice = input('Enter your choice of dinosaur ')
        if dinosaur_choice == '0' or dinosaur_choice == '1' or dinosaur_choice == '2':
            dinosaur_choice = self.herd.dinosaurs[int(dinosaur_choice)]
        else:
            dinosaur_choice = input('Enter your choice of dinosaur ')
        return dinosaur_choice

    def show_robo_fighter_options(self):
        print('TEAM ROBOT! Pick your robot: ')
        count = 0
        for i in self.fleet.robots:
            if i.health > 0:
                print(f'{str(count)} for {i.name}. Remaining Health: {i.health}')
                count += 1
        robot_choice = input('Enter your choice of robot ')
        if robot_choice == '0' or robot_choice == '1' or robot_choice == '2':
            robot_choice = self.fleet.robots[int(robot_choice)]
        else:
            robot_choice = input('Enter your choice of dinosaur ')
        return robot_choice
        

    def health_calculation(self):
        total_health_dino = 0
        total_health_robot = 0
        keep_playing = True
        for i in self.fleet.robots:
            if i.health > 0:
                total_health_robot += i.health
        for i in self.herd.dinosaurs:
            if i.health > 0:
                total_health_dino += i.health
        if total_health_dino <= 0 or total_health_robot <= 0:
            keep_playing = False
        return keep_playing

    def display_winners(self):
        total_health_dino = 0
        total_health_robot = 0
        winner = ''
        for i in self.fleet.robots:
            if i.health > 0:
                total_health_robot += i.health
        for i in self.herd.dinosaurs:
            if i.health > 0:
                total_health_dino += i.health
        if total_health_dino > 0:
            winner = 'Team Dinosaur'
        else:
            winner = 'Team Robot'
        print(f'The winner is {winner}!!!!')

    def run_game(self):
        #display a welcome message
        self.display_welcome() 

        #pick fighters and battle while both teams have health above zero
        while self.health_calculation() == True:
            self.battle()
            self.health_calculation()

        #display winner
        if self.health_calculation() == False:
            self.display_winners()
        
        
      
       
        
