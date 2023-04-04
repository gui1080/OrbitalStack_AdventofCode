# --- Day 1: Calorie Counting ---

# The code's input is in the "input.txt" file
input_file = open('input.txt', 'r')

# get all the lines in the input
Lines = input_file.readlines()

input_file.close()

# the elf the code is currently computing
current_elf = 0

# the one carrying more food (calories)
strongest_elf = 0

for line in Lines:

    # if the line is not empty...
    if line != "\n":

        # accumulate calories
        current_elf = current_elf + int(line)

    else:

        # is this elf carrying more calories?
        if current_elf > strongest_elf:

            strongest_elf = current_elf

        current_elf = 0

print("Strongest elf is carrying " + str(strongest_elf) + " calories!")