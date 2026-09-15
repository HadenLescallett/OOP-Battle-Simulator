from goblin import Goblin
from hero import Hero

ARENA_NAME = "The Final Stand"

def battle(hero: Hero, enemy: Goblin):
    while hero.is_alive() and enemy.is_alive():
        hero_damage = hero.attack()
        enemy.take_damage(hero_damage)
        if enemy.is_alive():
            enemy_damage = enemy.attack()
            hero.take_damage(enemy_damage)
    if hero.is_alive():
        print(f"{hero.name} won the battle!")
    else:
        print(f"{enemy.name} won the battle!")



def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The Monsters have awoken and the arena is set...")

    goblinOne = Goblin("Dingleberry")

    print(f"{goblinOne.name} enters the arena with {goblinOne.health}hp.")

    goblinTwo = Goblin("DingleCherry")

    print(f"{goblinTwo.name} enters the arena with {goblinTwo.health}hp.")

    print("But no hero has answered the call... yet.")
    
    hero = Hero("Link")

    battle(hero, goblinOne)


if __name__ == "__main__":
    main()
