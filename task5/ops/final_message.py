
# for every column in the stack, 
# pop() last element if column is not empty
def get_final_message(final_stack):
    
    final_message = ""

    for column in final_stack:

        if len(column) != 0:

            x = column.pop()
            final_message += x
    
    return final_message
