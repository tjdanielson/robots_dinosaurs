from Dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()
    
    #creates a herd of dinosaurs
    def create_herd(self):
        dino_one = Dinosaur('Rex the T-Rex', 20)
        dino_two = Dinosaur('Petr the Pterodactyl', 15)
        dino_three = Dinosaur('Vela the Velociraptor', 15)
        self.dinosaurs.append(dino_one)
        self.dinosaurs.append(dino_two)
        self.dinosaurs.append(dino_three)
        




