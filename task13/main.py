# --- Day 13: Distress Signal ---

from ops.comparison import compare

# The code's input is in the "input.txt" file
input_file = open('input_test.txt', 'r')

# get all the lines in the input, splitting "\n"
Lines = input_file.read().split("\n\n")

input_file.close()

print("\n-----------------------\n")

# Parsing the input
# (probably the hardest part of this task)
# At this point, every list pair is a string like "[1,1,3,1,1]\n[1,1,5,1,1]"
print("\nParse process\n")
print(Lines)

Lines = [i.splitlines() for i in Lines]
# Now, every element is divided like "[1,1,3,1,1]", "[1,1,5,1,1]"
# As a list of lists

print("\n")
print(Lines)

# eval turns the strings into integers
# for every string in line, for every char in every string
Lines = [ eval(j) for i in Lines for j in i ]

print("\n")
print(Lines)

# now the input is something like: "[1, 1, 3, 1, 1], ..."

final_data = []
temp = []

# make groups of two, for coherence
for i in range(len(Lines)):
    
    # first element of pair
    if i % 2 == 0:
        temp.append(Lines[i])
    # second element of pair
    else:

        temp.append(Lines[i])
        final_data.append(temp)
        temp = []

print("\n")
print(final_data)
print("\n-----------------------\n")

print(compare(final_data[0][0], final_data[0][1]))
print(compare(final_data[1][0], final_data[1][1]))
print(compare(final_data[2][0], final_data[2][1]))
print(compare(final_data[3][0], final_data[3][1]))
print(compare(final_data[4][0], final_data[4][1]))
print("\n")
print(compare(final_data[5][0], final_data[5][1]))
print(compare(final_data[6][0], final_data[6][1]))
print(compare(final_data[7][0], final_data[7][1]))
