# --- Day 25: Full of Hot Air ---
# Base 5 number conversion

# The code's input is in the "input.txt" file
input_file = open('input_test.txt', 'r')

# get all the lines in the input
List = input_file.readlines()

input_file.close()

NumberList = []

for line in List:
    NumberList.append(str(line).replace("\n", " ").replace(" ", ""))

'''

To sum up what really matters about this problem

    Decimal          SNAFU
        -2             =
        -1             -
        0              0
        1              1
        2              2
        3             1=    < no more elements, 
        4             1-       adds one to the left
        5             10       and keeps counting
        6             11
        7             12
        8             2=    < 5 elements later, 
        9             2-       1 becomes 2, and so on

So, It should be possible to perform operations just like
base 10 numbers.

        1=
    +   1- 
    -------
        =    -> (-3) > = (carry on -1)
    20       -> 20 in SNAFU is 10 in decimal. 
                Minus 1 from carry on, 9, minus 2, final total 7

'''

SNAFU_DEC = {
    "2": 2,
    "1": 1,
    "0": 0,
    "-": -1,
    "=": -2
}

DEC_SNAFU = {
    2: "2",
    1: "1",
    0: "0",
    -1: "-",
    -2: "="
}

longest_digit = 0
carry_on = 0
result = ""

for Number in NumberList:
    if len(Number) > longest_digit:
        longest_digit = len(Number)

# Sum starts from right to left
#   NumberList[0][longest_digit] 
# + NumberList[1][longest_digit]
# ... 

for column in range(longest_digit):

    sum_column = carry_on

    # reset carry_on
    carry_on = 0 
    
    for Number in NumberList:

        # this number is long enough
        # so It has a digit that should be added
        if column < len(Number):
            
            sum_column = sum_column + SNAFU_DEC[Number[len(Number) - 1 - column]]

    # If that column's sum is greater than 2?
    if sum_column > 2: 

        while sum_column > 2:
            
            # plus one to the column to the left
            carry_on += 1

            # plus one on the left 
            # equals - five on the right
            sum_column -= 5
    
    # What If the digit comes out negative?
    # It's going to be the same thing, but "backwards"
    else:

        while sum_column < -2: 
            
            # minus one to the column to the left
            carry_on -= 1

            # minus one on the left 
            # equals + five on the right
            sum_column += 5
    # and as numbers get bigger, this add/subtraction 
    # operation gets bigger and bigger

    result += DEC_SNAFU[sum_column]

print("Final result\n")
print(result[::-1])
print("\n")

result += DEC_SNAFU[carry_on]

print("Final result + carry on\n")  # this was needed for 10_snafu + 20_snafu
print(result[::-1])                 # (len(2) + len(2) = len(3))
print("\n")                         # as the last char was missing
