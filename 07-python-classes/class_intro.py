class Monster:
    # attributes
    health = 90
    energy = 40

    # methods
    def attack(self):
        print("The monster has attacked!")

    # exercise speed method
    def speed(self, movement):
        print(f"The monster has moved at {movement} speed!")


monster = Monster()
print(monster.health)
print(monster.energy)

monster.attack()
monster.speed(35)
