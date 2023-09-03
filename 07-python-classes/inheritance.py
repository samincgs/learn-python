# one class gets the attributes and methods from another class


class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    def attack(self, amount):
        print("The monster has attacked!")
        print(f"{amount} of damage has been dealt")
        self.energy -= 20

    def move(self, speed):
        print("The monster has moved")
        print(f"It has a speed of {speed}")


class Shark(Monster):
    def __init__(self, health, energy, speed):
        super().__init__(health, energy)
        self.speed = speed

    def bite(self):
        print("The shark bites!")

    def move(self):
        print("The shark has moved")
        print(f"It has a speed of {self.speed}")


shark = Shark(speed=25, health=100, energy=50)
print(shark.speed)
print(shark.health)
print(shark.energy)

# exercise
# scorpion class that inherits from the monster
# health and energy from parent
# poison_damage attribute
# overwrite the damage method to show poison damage


class Scorpion(Monster):
    def __init__(self, health, energy, poison_damage):
        super().__init__(health, energy)
        self.poison_damage = poison_damage

    def attack(self):
        print(f"the scorpion has dealt {self.poison_damage} poison damage!")


scorpion = Scorpion(25, 15, 5)
scorpion.attack()
