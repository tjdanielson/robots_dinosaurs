from Robot import Robot
from Weapon import Weapon

class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()
    
    def create_fleet(self):
        robo_one = Robot('R2D2', Weapon('Paper Cutter', 10))
        robo_two = Robot('HAL', Weapon('Mind Conrol', 30))
        robo_three = Robot('Bender', Weapon('Broken Bottle', 20))
        self.robots.append(robo_one)
        self.robots.append(robo_two)
        self.robots.append(robo_three)
        #for testing:
        # for i in self.robots:
        #     print(i.name + i.weapon.name)

# for testing:
#fleet = Fleet()