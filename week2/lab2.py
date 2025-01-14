import random

elements = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon"]
print("Elements: ", elements)
# git add . && git commit -m "add elements array" && git push

#def funct_name():
#   return True
#def say_greeting(name, message="hi"):
#    print(f"{message}, {name}")
#say_greeting("Ricki")
#say_greeting("Ricki", "Hello")

def get_valid_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Please enter a valid integer")
            continue
try:
    elements_selected = get_valid_int_input("Enter the index of the element you would like to select: ")
    # Roll dice
    elementRoll = random.randint(1,6)
    totalNum = elements_selected + elementRoll

    # Print the result based on the totalNum
    if elementRoll <= 2:
        print("You rolled a weak element, fren.")
    elif elementRoll <= 4:
        print("You rolled a mid element, fren.")
    else:
        print("You rolled a strong element, fren.")
except IndexError:
    print("Error: Invalid element index!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")