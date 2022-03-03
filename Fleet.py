from Robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []
    
    def create_fleet(self):
        robo_one = Robot('R2D2')
        robo_two = Robot('HAL')
        robo_three = Robot('Bender')
        self.robots.append(robo_one)
        self.robots.append(robo_two)
        self.robots.append(robo_three)