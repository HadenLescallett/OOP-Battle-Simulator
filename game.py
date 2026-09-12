from goblin import Goblin


ARENA_NAME = "The Final Stand"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The Monsters have awoken and the arena is set...")

    goblin = Goblin("Dingleberry")

    print(f"{goblin.name} enters the arena with {goblin.health}hp.")

    goblinTwo = Goblin("DingleCherry")

    print(f"{goblinTwo.name} enters the arena with {goblinTwo.health}hp.")

    print("But no hero has answered the call... yet.")


if __name__ == "__main__":
    main()
