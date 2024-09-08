# Character Class
from weapon import fists

class Character:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.max_health = health
        self.health = health
        
        self.weapon = fists
        
    def attack(self, target):
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        print(f'{self.name} dealth {self.weapon.damage} damage to {target.name} with {self.weapon.name}')
        
        
        
class Hero(Character):
    def __init__(self, name, health):
        super().__init__(name, health)
        self.default_weapon = self.weapon
        
    def equip(self, weapon):
        self.weapon = weapon
        print(f'{self.name} equipped a(n) {self.weapon.name}!')
        
    def drop(self):
        print(f'{self.name} dropped the {self.weapon.name}!')
        self.weapon = self.default_weapon
        

class Enemy(Character):
    def __init__(self, name, health, weapon):
        super().__init__(name, health)
        self.weapon = weapon
        