# --- Day 2: Rock Paper Scissors ---

from match import check_result, check_rigged_result

# The code's input is in the "input.txt" file
input_file = open('input.txt', 'r')

# get all the lines in the input
Lines = input_file.readlines()

input_file.close()

outcome = 0
outcome_rigged = 0
rounds = 1

print("-------------")
for line in Lines:

    print("Round - " + str(rounds))
    print(line)
    opponent = line[:2].replace(" ", "")
    player = line[2:3].replace(" ", "")

    outcome = outcome + check_result(opponent, player)
    outcome_rigged = outcome_rigged + check_rigged_result(opponent, player)
    rounds += 1
    print("-------------")

print("Final outcome (fair) - " + str(outcome))
print("Final outcome (rigged) - " + str(outcome_rigged))
print("-------------")
