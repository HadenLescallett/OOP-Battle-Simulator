import random
from enemy import Enemy

class Boss(Enemy):
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name, health = 300, attackPower = 30):
        self.name = name
        self.health = health
        self.attack_power = attackPower

    def attack(self):
        """Return a random amount of damage."""
        attackStyle = random.randint(1,2)
        if attackStyle == 1:
            print("ThunderStorm")
            return 5 * random.randint(1,3)
        else:
            print("Windwalker")
        return self.attackPower * random.randint(1, 2)

    def take_damage(self, damage):
        damage = damage * .75
        return super().take_damage(damage)