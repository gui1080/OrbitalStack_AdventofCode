# --- Day 5: Supply Stacks ---

from aux.instruct_parser import instructions_transformation
from aux.stack_parser import stack_transformation
from ops.stack_update import execute_op
from ops.final_message import get_final_message

# The code's input is in the "input.txt" file
input_file = open('input.txt', 'r')

# get all the lines in the input
Lines = input_file.readlines()

input_file.close()

# elements per index
my_stack = []

# intructions for moving elements 
# between stacks 
instructions = []

reading_stack = True

for line in Lines:
    
    # if the line is not empty...
    if line == "\n":
        reading_stack = False

    # from the stacks to the instructions
    # there will always be one empty line

    if reading_stack == True:
        my_stack += [line]
    
    elif reading_stack == False and line != "\n":
        instructions += [line]

# Gets my stack into a decent structure
# ------------------------------

final_stack = stack_transformation(my_stack)

print("The stack \n\n")
print(final_stack)
print("Len - " + str(len(final_stack)))
print("-----------\n")

# Instruction parser
# ------------------------------

final_instructions = instructions_transformation(instructions)

print("Instructions \n\n")
print(final_instructions)
print("Len - " + str(len(final_instructions)))
print("-----------\n")

# Decided to don't use numpy because of errors regarding
# lists of lists that have different len() values

# Operations!
# ------------------------------

for i in range(len(final_instructions)):
    temp_stack = final_stack
    final_stack = execute_op(temp_stack, final_instructions[i])

print("This is how the stack looks like be the end of the operations!\n\n")
print(final_stack)
print("-----------\n")

# Gets the final message
# ------------------------------

final_message = get_final_message(final_stack)
print("This is the final message!")
print(final_message)
print("-----------\n")

# ------------------------------
