import random
from goblin import Goblin

class Hero:
    def __init__ (self, name):
        self.name = name
        self.health = 110
        self.attack_power = 20

    def attack(self):
        PassedCritCheck = (1,6) == 6
        if PassedCritCheck:
            return random.randint(1,self.attack_power) * 1.25
            print("The Hero Got a Critical hit")
        return random.randint(1, self.attack_power)

    def take_damage(self, damage):
         self.health = max(0, self.health - damage)
         print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def is_alive(self):
        return self.health > 0

    #def Heros_Turn(self):
      #  GothamChess = Hero("GothamChess")
       # GothamChesssattacknumber = GothamChess.attack()
       # print("Gotham Chess arrives and attacks Magnus's Goblins...")
       # goblin.take_damage(GothamChesssattacknumber)

    pass
