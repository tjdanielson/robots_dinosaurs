# robots_dinosaurs
Using the concepts of OOP by creating classes and objects (instances of those classes) to interact with each other, create a console application that will have robots and dinosaurs fight in a battle.


Game Play Instructions:
My version of Robots vs Dinosaurs is intended to be a two player game - each player can play as either Team Robot or Team Dinosaur.
The game is formulated in a series of rounds until either team reaches 0 health points across their team.
Each round, both players have the opportunity to attack (unless the first attack kills a player).

Robots:
*Team Robot has a fleet of three robots - R2D2, HAL, and Bender.
*Robots come with weapons and each weapon has a different 'Attack Power' - they default as follows:
***R2D2 -- Paper Cutter (Attack Power: 10)
***HAL -- Mind Control (Attack Power: 30)
***BENDER -- Broken Bottle (Attack Power: 20)

Although they default as above, the fleet of robots share the weapons. You can choose to use any of the weapons with any of the fighters (you will be prompted to change before each round)

Dinosaurs:
*Team Dinosaur has a herd of three dinosaurs - Rex the T-Rex, Petr the Pterodactyl, and Vela the Velociraptor
*Dinosaurs' attack power is associated directly to the dinosaur as follows:
***Rex the T-Rex -- Attack Power: 30
***Petr the Pterodactyl -- Attack Power: 20
***Vela the Velociraptor -- Attack Power: 10

Before each round, Team Dinosaur must choose which attack they want their fighter to perform in the battle. The options are as follows:
*Eye Scratch
*Dive Bomb
*Bite

Health

Power/Energy:
Robots have 'Power Levels' and Dinosaurs have 'Energy Levels', starting at 30 points. Each time a fighter is sent into battle, that fighter loses 10 power/energy points. When the power/energy level hits zero, their health also drops to zero and they die. If this happens, it will be included in the results summary from the round. 

Game flow: 
ROUND ONE:
1. Team Dinosaur will be prompted to choose their fighter
2. Next, Team Dinosaur will be prompted to choose their attack
3. Team Robot will be prompted to choose their fighter
4. Next, Team Robot will be prompted to choose their weapon
4. Battle ensues! Dinosaur will attack first, then (if the robot was not killed) the Robot will counter attack. Results will be printed to the console - each Fighter loses points according to the attacks that occurred in the battle. If a fighter drops to zero health points, they are killed - this info will be included in the results.

ROUND TWO:
Same as round one, except now Team Robot goes first!

ROUNDS will continue until there is a winner (see winning section, below)

WINNING:
The game is over when all fighters on one team are killed (health points drop to zero). Both team's stats will be printed with the results.