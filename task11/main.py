# --- Day 11: Monkey in the Middle ---
# monke and OOP

from aux.monke_parser import get_monkey_info
from ops.monke_operation import monkey_test
from ops.monke_business import retireve_monkey_business_level
import model.monke

# The code's input is in the "input.txt" file
input_file = open('other_input.txt', 'r')

# get all the lines in the input
Lines = input_file.readlines()

input_file.close()

# Parse monkey info
monkey_data = get_monkey_info(Lines)

# ---------------------------------------------

''' 
monkey_data is an array of arrays 
every array in this array is a monkey description
['0'],          -> monkey index
['79', '98'],   -> monkey inventory
['*', '19'],    -> monkey operation
['23'],         -> monkey operation is divisible by this number?
['2'],          -> true = throw to this monkey
['3']           -> false = throw to this monkey

"monkey 0" tests 79
79 * 19 = 1501 // 3
500 is not divisible by 23
79 now belongs to monkey 3
'''

# It looks like this task wants me to demonstrate OOP concepts
# So, there is a monkey class in monke.py, inside of "model" folder

# Monkey objects!
# ---------------------------------------------

monkey_objects = []

for this_monkey in monkey_data:
    monkey_objects.append(model.monke.Monke(this_monkey))

# Monkey business!
# ---------------------------------------------
for x in range(20):

    for monkey in range(len(monkey_objects)):

        print("------")
        if monkey_objects[monkey].is_inventory_empy() == False:

            inventory = monkey_objects[monkey].get_inventory()
            print("Inventory - " + str(inventory))

            print("---------")
            for i in range(len(inventory)):
                print(inventory[i])
                test_result = monkey_test(monkey_objects, monkey_objects[monkey], inventory[i])
            print("---------")

    print("\n\n--------- Inventory ---------")
    print("End of round " + str(x+1))
    for monkey in range(len(monkey_objects)):
        print(monkey_objects[monkey].get_inventory())
    print("-----------------------------\n\n")

print("\n\n\n\n----- End of Iterations -----")
for monkey in range(len(monkey_objects)):
    print(monkey_objects[monkey].get_item_counter())
print("-----------------------------\n\n")

monkey_business_level = retireve_monkey_business_level(monkey_objects)
print(monkey_business_level)
