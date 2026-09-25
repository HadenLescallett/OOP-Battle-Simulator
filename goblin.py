import random
from enemy import Enemy


class Goblin(Enemy):
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        super().__init__(name, health = 100, attackPower = 8)
        self.gold = 0
       

    def steal(self, hero):
        """steal gold from hero"""
        self.gold = self.gold + hero.gold
        hero.gold = 0
        print("Get Wrecked Noob")
    
    def take_damage(self, damage):
        """Reduce health without allowing it to fall below zero."""
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def is_alive(self):
        """Return True while the goblin has health remaining."""
        return self.health > 0

    #def FirstGoblinsTurn(self):
       # GoblinOnesattackpower = goblin.attack()
       # print("Magnus's Goblin attacks the hero and...")
       # GothamChess.take_damage(GoblinOnesattackpower)