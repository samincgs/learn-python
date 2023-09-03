#  double underscore methods
class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    # def __len__(self):
    #     return 5

    # def __call__(self):
    #     return "The monster was called!"

    # def __add__(self, other):
    #     return self.health + other

    def __str__(self):
        print(f"The energy of the current character is {self.energy}")

    def attack(self, dmg):
        print("The monster attacked!")
        print(f"{dmg} was dealth")
        self.energy -= 20
        print(self.energy)

    def move(self, speed):
        print("The monster has moved!")
        print(f"It has a speed of {speed}")


monster = Monster(health=50, energy=20)
# print(len(monster))
# print(monster())
# print(monster + 20)
monster.__str__()
