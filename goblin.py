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
        
    #def FirstGoblinsTurn(self):
       # GoblinOnesattackpower = goblin.attack()
       # print("Magnus's Goblin attacks the hero and...")
       # GothamChess.take_damage(GoblinOnesattackpower)