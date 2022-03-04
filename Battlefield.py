from Fleet import Fleet
from Herd import Herd

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def display_welcome(self):
        print('Welcome to ROBOTS vs DINOSAURS!!')

    def battle(self):
        dino_start = True #BUG: resets to True every time. dino_start needs to live somewhere else
        dinosaur_choice = self.show_dino_fighter_options()
        dinosaur_attack = self.choose_attack()
        robot_choice = self.show_robo_fighter_options()
        self.change_weapon(robot_choice)
        print('****************************************')
        print('READY...SET...BATTLE!!!')
        print('****************************************')
        if dino_start == True:
            self.dino_turn(dinosaur_choice, robot_choice, dinosaur_attack)
            if robot_choice.health == 0:
                print(f'{robot_choice.name} died, ending the round.')
            else: 
                self.robo_turn(robot_choice, dinosaur_choice)
            dino_start = False  
        else:
            self.robo_turn(robot_choice, dinosaur_choice)
            if dinosaur_choice.health == 0:
                print(f'{dinosaur_choice.name} died, ending the round.')
            else:
                self.dino_turn(dinosaur_choice, robot_choice)
            dino_start = True


        
    def dino_turn(self, dinosaur_choice, robot_choice, dinosaur_attack):
        print('DINOSAUR\'S TURN')
        dinosaur_choice.attack(robot_choice, dinosaur_attack)
        

    def robo_turn(self, robot_choice, dinosaur_choice):
        print('ROBOT\'S TURN')
        robot_choice.attack(dinosaur_choice)
    

    def show_dino_fighter_options(self):
        print('****************************************')
        print('TEAM DINOSAUR! Pick your dinosaur: ')
        for i in self.herd.dinosaurs:
            if i.health > 0:
                print(f'{str(self.herd.dinosaurs.index(i))} for {i.name}. Remaining Health: {i.health}')
        dinosaur_choice = input('Enter your choice of dinosaur ')
        while dinosaur_choice != '0' and dinosaur_choice != '1' and dinosaur_choice != '2':
            dinosaur_choice = input('Enter your choice of dinosaur ')
        if dinosaur_choice == '0' or dinosaur_choice == '1' or dinosaur_choice == '2':
            dinosaur_choice = self.herd.dinosaurs[int(dinosaur_choice)]  
        return dinosaur_choice

    def show_robo_fighter_options(self):
        print('****************************************')
        print('TEAM ROBOT! Pick your robot: ')
        for i in self.fleet.robots:
            if i.health > 0:
                print(f'{str(self.fleet.robots.index(i))} for {i.name}. Remaining Health: {i.health}')
        robot_choice = input('Enter your choice of robot ')
        while robot_choice != '0' and robot_choice != '1' and robot_choice != '2':
            robot_choice = input('Enter your choice of robot ')
        if robot_choice == '0' or robot_choice == '1' or robot_choice == '2':
            robot_choice = self.fleet.robots[int(robot_choice)]
        return robot_choice

    def change_weapon(self, robot_choice):
        print(f'TEAM ROBOT, {robot_choice.name}\'s current weapon is {robot_choice.weapon.name} - do you want to change it?')
        weapon_change = input('Change weapon? Y/N ')
        while weapon_change != 'Y' and weapon_change != 'N':
            weapon_change = input('Change weapon? Y/N ')
        if weapon_change == 'Y':
            self.fleet.weapon_swap(robot_choice)
    
    def choose_attack(self):
        attack_tuple = ("Eye Scratch", "Dive Bomb", "Bite")
        print(f'TEAM DINOSAUR, choose your attack!')
        count = 0
        for i in attack_tuple:
            print(f'{str(count)} for {i}.')
            count += 1
        attack_choice = input('Choose your attack ')
        while attack_choice != '0' and attack_choice != '1' and attack_choice != '2':
            attack_choice = input('Choose your attack ')
        if attack_choice == '0' or attack_choice == '1' or attack_choice == '2':
            attack_choice = attack_tuple[int(attack_choice)]
        return attack_choice
         

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
        print('****************************************')
        print('WE HAVE A WINNER.....')
        total_health_dino = 0
        total_health_robot = 0
        winner = ''
        print('STATS:')
        for i in self.fleet.robots:
            print(f'Robot: {i.name} Remaining Health: {i.health}')
            if i.health > 0:
                total_health_robot += i.health
        for i in self.herd.dinosaurs:
            print(f'Dinosaur: {i.name} Remaining Health: {i.health}')
            if i.health > 0:
                total_health_dino += i.health
        if total_health_dino > 0:
            winner = 'TEAM DINOSAUR'
        else:
            winner = 'TEAM ROBOT'
        print('****************************************')
        print(f'THE WINNER IS {winner}!!!!')

    def run_game(self):
        #display a welcome message
        self.display_welcome() 

        #pick fighters and battle while both teams have health above zero
        while self.health_calculation() == True:
            self.battle()

        #display winner
        if self.health_calculation() == False:
            self.display_winners()
        
        
      
       
        
