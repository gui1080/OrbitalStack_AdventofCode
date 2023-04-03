import re 

# turn
# "move 1 from 2 to 1"
# into
# "ammount, origin index, destination index"
# or [1, 1, 0]

def instructions_transformation(instructions):

    final_instructions = []

    for i in range(len(instructions)):

        current_instruction = re.findall("[0-9]", instructions[i])
        current_instruction = [int(inst) for inst in current_instruction]
        current_instruction[1] = current_instruction[1] - 1
        current_instruction[2] = current_instruction[2] - 1
        final_instructions.append(current_instruction)


    return final_instructions