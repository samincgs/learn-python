class Monster:
    """A monster class that provides utility"""

    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

        # private attributes
        self._id = 5

    def attack(self, amount):
        print("The monster has attacked!")
        print(f"{amount} of damage has been dealt")
        self.energy -= 20

    def move(self, speed):
        print("The monster has moved")
        print(f"It has a speed of {speed}")


monster = Monster(20, 10)


# hasattr and setattr
print(hasattr(monster, "health"))
setattr(monster, "weapon", "Sword")
print(vars(monster))

# doc
print(monster.__doc__)
