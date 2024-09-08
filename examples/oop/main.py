# simulate an rpg character, weapon and health fight with objects
from character import Character, Hero, Enemy
from weapon import short_bow, iron_sword

hero = Hero(name='Hero', health=100)
hero.equip(iron_sword)
enemy = Enemy(name='Enemy', health=100, weapon=short_bow)

while True:
    hero.attack(enemy)
    enemy.attack(hero)
    
    print(f'{hero.name}"s Health: {hero.health}')
    print(f'{enemy.name}"s Health: {enemy.health}')
    
    input() 
    
    