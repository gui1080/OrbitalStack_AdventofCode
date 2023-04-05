# --- Day 13: Distress Signal ---
# Recursion and Sorting Algorithms!

from ops.comparison import compare
from ops.sort import bubblue_sort

# The code's input is in the "input.txt" file
input_file = open('input_test.txt', 'r')

# get all the lines in the input, splitting "\n"
Lines = input_file.read().split("\n\n")

input_file.close()

# ---------------------------------------------
# Parsing the input
# At this point, every list pair is a string like "[1,1,3,1,1]\n[1,1,5,1,1]"

Lines = [i.splitlines() for i in Lines]
# Now, every element is divided like "[1,1,3,1,1]", "[1,1,5,1,1]"
# As a list of lists

# eval turns the strings into integers
# for every string in line, for every char in every string
Lines = [ eval(j) for i in Lines for j in i ]

# now the input is something like: "[1, 1, 3, 1, 1], ..."
# This will be useful later, when the task is to organize the input
SortingInput = Lines

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

# ---------------------------------------------
# Comparing the elements

acc_index = 0

for i in range(len(final_data)):
    
    result = compare(final_data[i][0], final_data[i][1])
    if result == "right":
        acc_index += (i + 1)

print("Final output - " + str(acc_index))

# Sorting the input
# ---------------------------------------------

# append new elements!
# "dividers"
SortingInput.append([[2]])
SortingInput.append([[6]])

# sort the input
# Literally using the normal implementation of Bubble Sort
# But using my function to compare two lists at a time
bubblue_sort(SortingInput)

# find the divider's index
# sum 1
# multiply 
# that's the answer!
for i in range(len(SortingInput)):
    if SortingInput[i] == [[2]]:
        a = i + 1
    if SortingInput[i] == [[6]]:
        b = i + 1

print("Divider's positions multiplied - " + str(a * b))

# ---------------------------------------------
