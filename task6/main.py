# --- Day 6: Tuning Trouble ---

# given string, find position 
# where last 4 characters are different

# The code's input is in the "input.txt" file
input_file = open('input.txt', 'r')

# get the input (1 line signal)
datastream = input_file.readline()

input_file.close()

# ---------------------------------------

# string index, for every char processed
count = 1

current_data = ""

for char in datastream:

    if char != "\n":

        # first few occurences
        # getting partial datastream
        if len(current_data) < 4:

            current_data = current_data + char

        else:

            # oldest char goes out
            # new char is appended
            current_data = current_data[1:] + char

            # if this is true, there are no repeated characters
            if len(set(current_data)) == len(current_data):
                break
            
        count += 1

print(str(count) + " characters need to be processed before the first start-of-message marker is detected!")