from Dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()
    
    def create_herd(self):
        dino_one = Dinosaur('Rex the T-Rex', 30)
        dino_two = Dinosaur('Petr the Pterodactyl', 20)
        dino_three = Dinosaur('Vela the Velociraptor', 10)
        self.dinosaurs.append(dino_one)
        self.dinosaurs.append(dino_two)
        self.dinosaurs.append(dino_three)
        # for testing:
        # for i in self.dinosaurs:
        #     print(i.name)

#for testing:
herd = Herd()




