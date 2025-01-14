import random

weapons = ["Fist", "Knife", "Club", "Gun", "Bomb","Nuclear Bomb"]
print(weapons)

def get_valid_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Please enter a valid integer.")
            continue
try:
    selected_weapon = get_valid_input("Enter the index of the weapon you would like to use: ")

    # Roll Dice
    weaponRoll = random.randint(1,6)
    hero_combat_strength = weaponRoll + selected_weapon
    print(f"Your hero combat strength is {hero_combat_strength}")

    # Print result
    if weaponRoll <= 2:
        print("You rolled a weak weapon, fren!")
    elif weaponRoll <= 4:
        print("Your weapon is meh!")
    else:
        print("Nice weapon, fren!")

    if weaponRoll != weapons[0]:
        print("Thank goodness you didn't roll the Fist")
except IndexError:
    print("Error: Enter a valid index!")
except Exception as e:
    print(f"Error: An unexpected error occurred: {e}")







