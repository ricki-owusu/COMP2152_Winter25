# functions_lab05.py
import random


# Question 3
def collect_loot(loot_options, belt):
    print("Random loot process:")
    loot_roll = random.choice(range(1, len(loot_options) + 1))
    loot = loot_options.pop(loot_roll - 1)
    print("    |    Your belt: ", belt)
    return loot_options, belt

# Question 4 Use Loot
def use_loot(belt, health_options):
    good_loot_options = ["Health Potion", "Leather Boots"]
    bad_loot_options = ["Poison Potion"]

    print("You see a monster! So you quicly use your first item: ")

    first_item = belt.pop(0)
    if first_item in good_loot_options:
        health_options = min(20, (health_options + 2))
        print("You use your first item: " + first_item + "and your health is: " + str(health_options))
    elif first_item in bad_loot_options:
        health_options = max(20, (health_options - 2))
        print("You use your first item: " + first_item + "and your health is: " + str(health_options))
    else:
        print("You used your first item: " + first_item + "and it was not helpful")
        return belt, health_options