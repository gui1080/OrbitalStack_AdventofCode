import numpy as np

def execute_op(final_stack, instruction):

    # stack is a variable that looks like this:
    # stack =  [[Z, N]     
    #           [M, C, D]  
    #           [P]]   

    # instruction
    # [x, y, z] -> x elements
    # go from y index to z index

    for i in range(instruction[0]):
        #if len(final_stack[instruction[1]]) != 0:
        temp = final_stack[instruction[1]].pop()
        final_stack[instruction[2]].append(temp)

    return final_stack