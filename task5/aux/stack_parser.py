# turn this
# ['    [D]    \n', 
#  '[N] [C]    \n', 
#  '[Z] [M] [P]\n', 
#  ' 1   2   3 \n']
# into
# stack =  [[Z, N]     -> 0
#           [M, C, D]  -> 1
#           [P]]       -> 2
#
# Assuming that the stack may be variable

def stack_transformation(my_stack):

    final_stack = []

    coordinates_index = len(my_stack) - 1 

    for column in range(len(my_stack[coordinates_index])):
        
        new_entry = []
        char = my_stack[coordinates_index][column]
        
        if char != " " and char != "\n":
            # found a valid column

            for i in range(0, coordinates_index):

                current_line = my_stack[i]
                
                if current_line[column] != " " and current_line[column] != "\n":
                    new_entry.append(current_line[column])
                
            final_stack.append(new_entry)


    for i in range(len(final_stack)):
        temp = list(reversed(final_stack[i]))
        final_stack[i] = temp
    
    return final_stack