# Jade Watson
# 05/25/2023
# This file shows that Alex has found the lost item and he is trying to escape from danger
# he is coming across in the game


# Import necessary modules and files
import main_character_TEMPLATE
import battle_TEMPLATE as battle

def start(player):
    print("Alex has discovered the long-lost item, but he is not alone.")
    print("A rival treasure hunter party has also uncovered the artifact and is determined to seize it.")
    print("Alex must struggle to defend the relic and survive in the wild.")
    print("")

    # Give the player some options
    print("What would you like to do?")
    print("1. Fight the competing treasure hunters")
    print("2. Sneak past them to escape")

    # Get the player's choice
    choice = input("Enter your choice: ")

    # Process the player's choice
    if choice == "1":
        # Player chooses to fight the treasure hunters
        print("You choose to fight the treasure hunters.")
        print("Prepare for battle!")

        # Call the battle module to initiate a battle
        battle.attack(player)

        # Check if the player survived the battle
        if player.hp <= 0:
            print("You lost the battle and died. Game over.")
            exit()
        else:
            print("You defeated the treasure hunters and protected the relic!")
    elif choice == "2":
        # Player chooses to sneak past the treasure hunters
        print("You choose to sneak past the treasure hunters.")
        print("Stealthily navigate through the area to avoid detection.")

        # TODO: Implement sneaking mechanics and potential obstacles

        print("You successfully escaped the treasure hunters and kept the relic!")
    else:
        print("Invalid choice. Please choose a valid option.")

    # Move to the next section
    import section_4_TEMPLATE
    section_4_TEMPLATE.start(player)
