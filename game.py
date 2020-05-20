# Import modules
import time
import random


# Define functions
def print_pause(s):
    print(s)
    time.sleep(2)


def print_pause_long(s):
    print(s)
    time.sleep(3)


def main():
    global items
    items = ["dagger"]
    global enemy
    enemy = random.choice(enemies)
    # Introduction
    print_pause_long("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    print_pause_long(f"Rumor has it that a {enemy} is somewhere around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house")
    print_pause("To your right is a dark cave")
    print_pause("In your hand you hold your trusty (but not very effective) dagger")
    field()


def field():
    # Things that happen when the player runs back to the field
    print("\nEnter 1 to knock on the door of the house.")
    print("Enter 2 to peek into the cave.")
    print("\nWhat would you like to do?")
    choice1 = input("(Please enter 1 or 2).\n")
    while True:
        if choice1 == '1':
            house()
            break
        elif choice1 == '2':
            cave()
            break
        else:
            choice1 = input("(Please enter 1 or 2).\n")


def cave():
    # Things that happen to the player goes in the cave
    print_pause("You peer cautiously into the cave.")
    if "sword" in items:
        print_pause("You've been here before, and gotten all the good stuff. It's just an empty cave now.")
        print_pause("You walk back out to the field")
    elif "sword" not in items:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take the sword with you.")
        items.append("sword")
        items.remove("dagger")
        print_pause("You walk back out to the field")
    field()


def house():
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door opens and out steps the {enemy}.")
    print_pause(f"Eep! This is the {enemy}'s house!")
    print_pause(f"The {enemy} attacks you!")
    if "sword" not in items:
        print_pause("You feel a bit under-prepared for this, what with only having a tiny dagger.")
    print("\nEnter 1 to fight.")
    print("Enter 2 to run away.")
    print("\nWhat would you like to do?")
    choice2 = input("(Please enter 1 or 2).\n")
    while True:
        if choice2 == '1' and "sword" in items:
            won()
            break
        elif choice2 == '1' and "sword" not in items:
            lost()
            break
        elif choice2 == '2':
            print_pause("You run back into the field. Luckily, you don't seem to have been followed.")
            field()
            break
        else:
            choice2 = input("(Please enter 1 or 2).\n")


def won():
    print_pause(f"As the {enemy} moves to attack, you unsheath your new sword.")
    print_pause("The Sword of Ogoroth shines brightly in your hand as you brace yourself for the attack.")
    print_pause(f"But the {enemy} takes one look at your shiny new toy and runs away")
    print_pause(f"You have rid the town of the {enemy}. You are victorious!")
    play_again()


def lost():
    print_pause("You do your best...")
    print_pause(f"But your dagger is no match for the {enemy}.")
    print_pause("You have been defeated!")
    play_again()


def play_again():
    print("\nWould you like to play again?")
    choice3 = input("(Please enter 'y' or 'n').\n")
    while True:
        if choice3 == 'y':
            print_pause("Excellent, restarting the game...")
            main()
            break
        elif choice3 == 'n':
            break
        else:
            choice3 = input("(Please enter 'y' or 'n').\n")


# Global variable
enemies = ["fire dragon", "giant troll", "poisonous pirate"]
enemy = "undefined"
# Launch the game
main()