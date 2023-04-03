import aux.circular_linked_list

# The code's input is in the "input.txt" file
input_file = open('test_input.txt', 'r')

# get all the lines in the input
Lines = input_file.readlines()

operations = []

nums = aux.circular_linked_list.CLL()

# If It is needed to get a index given a node's value
# It is necessary to know that data's occurence
historic = []

for line in Lines:
    
    # if the line is not empty...
    if line != "\n":
        operations.append(int(line))
        nums.append(int(line))

for op in operations:

    print("-------\n\n\n")

    print(nums)

    if op > 0:
        occur = historic.count(op)
        if occur == 0:
            print("Moving - " + str(op) + "\nIndex - " + str(nums.index_by_data(op)) + "\n")
            nums.move_positive(nums.index_by_data(op))
        else:
            print("Moving - " + str(op) + "\nIndex - " + str(nums.index_by_data(op+1)) + "\n")
            nums.move_positive(nums.index_by_data(op+1))

        historic.append(op)

    if op < 0:
        occur = historic.count(op)
        if occur == 0:
            print("Moving - " + str(op) + "\nIndex - " + str(nums.index_by_data(op)) + "\n")
            nums.move_negative(nums.index_by_data(op))

        else:
            print("Moving - " + str(op) + "\nIndex - " + str(nums.index_by_data(op+1)) + "\n")
            nums.move_negative(nums.index_by_data(op+1))

        historic.append(op)

    print(nums)

print(nums.node_from_zero(1000).data)
print(nums.node_from_zero(2000).data)
print(nums.node_from_zero(3000).data)
