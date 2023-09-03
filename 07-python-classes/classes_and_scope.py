# scope problem
# with functions
# health = 10


# def update_health(amount):
#     global health
#     health += amount


# print(health)
# update_health(20)
# print(health)


class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = self.set_energy(energy)

    def update_energy(self, amount):
        self.energy += amount

    def set_energy(self, energy):
        new_energy = energy * 2
        return new_energy

    def get_damage(self, amount):
        self.health -= amount


# print(monster.energy)

# create a hero class with 2 parameters: damage, monster
# the monster class should have a method that lowers the health -> get_damage(amount) reduce from monster
# the hero class shold have an attack method that calls the get_damage method from the monster
# the amount of damage is hero_damage


class Hero:
    def __init__(self, damage, monster):
        self.damage = damage
        self.monster = monster

    def attack(self):
        self.monster.get_damage(self.damage)


monster = Monster(100, 50)
hero = Hero(15, monster)
hero.attack()
print(monster.health)
