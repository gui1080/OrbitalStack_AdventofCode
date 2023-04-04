# --- Day 10: Cathode-Ray Tube ---
# "Elvish Assembly"

# Did something like this back in unversity
# But It was a translator from an imaginary Assembly
# language to IA-32. Overall learned a lot of Assembly in school.

import re 
from ops.signal import check_signal

# The code's input is in the "input.txt" file
input_file = open('input2.txt', 'r')

# get all the lines in the input
Lines = input_file.readlines()

input_file.close()

cycles = 1
x = 1
signal_strength = 0

for line in Lines:

    if "noop" in line:
        print("noop")
        
        # noop starts

        print("--------------")
        print("Cycle " + str(cycles))
        print("X value " + str(x))
        
        # check strength
        new_strength = check_signal(cycles, x)
        signal_strength = signal_strength + new_strength
        
        # next cycle
        cycles += 1

    elif "addx" in line:

        if "-" in line:

            # subtract
            print(line)

            # operation starts! 
            # -------------------

            print("--------------")
            print("Cycle " + str(cycles))
            print("X value " + str(x))
            

            # x value was not updated yet
            # check cycle
            new_strength = check_signal(cycles, x)
            signal_strength = signal_strength + new_strength

            # next cycle
            cycles += 1

            # -------------------

            print("--------------")
            print("Cycle " + str(cycles))
            print("X value " + str(x))
            
            # check cycle
            new_strength = check_signal(cycles, x)
            signal_strength = signal_strength + new_strength

            # x is going to be updated at the end of the cycle
            # end of cycle

            op_value = int(re.findall("[0-9]+", line)[0])
            x = x - op_value

            # next cycle
            cycles += 1

            # operation finished, took 2 cycles
            # -------------------

        else:

            # sum
            print(line)

            # operation starts! 
            # -------------------

            print("--------------")
            print("Cycle " + str(cycles))
            print("X value " + str(x))
            

            # x value was not updated yet
            # check cycle
            new_strength = check_signal(cycles, x)
            signal_strength = signal_strength + new_strength

            # next cycle
            cycles += 1

            # -------------------

            print("--------------")
            print("Cycle " + str(cycles))
            print("X value " + str(x))

            # check cycle
            new_strength = check_signal(cycles, x)
            signal_strength = signal_strength + new_strength

            # x is going to be updated at the end of the cycle
            # end of cycle
            op_value = int(re.findall("[0-9]+", line)[0])
            x = x + op_value

            # next cycle
            cycles += 1
            
            # operation finished, took 2 cycles
            # -------------------


print("-------------- END --------------")
print("Cycle " + str(cycles))
print("X value " + str(x))
print("--------------")

print(signal_strength)
