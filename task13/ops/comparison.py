
# this function compares "a" and "b"
# even If "a" or "b" is a list
# If It is a list, recursion starts
# until base case happens: comparing two integers
def compare(a, b):

    # one iteration from base case
    # the input will be two integers
    # ----------------------------------

    # if one element is a list
    # and the other is an integer
    if (type(a) == list) and (type(b) == int):
        #print("Comparing a list and an integer")
        result = compare(a, [b])
        return result

    elif (type(a) == int) and (type(b) == list):
        #print("Comparing an integer and a list")
        result = compare([a], b)
        return result

    # base case
    # ----------------------------------

    # If both elements are integers, nothing else to do
    # just compare
    elif (type(a) == int) and (type(b) == int):
        
        #print("Comparing two integers")

        if a < b:
            return("right")
        elif a > b:
            return("left")
        elif a == b:
            return("equal")

    # two lists
    # ----------------------------------

    elif (type(a) == list) and (type(b) == list):
        
        #print("Comparing two lists")

        result = "equal"

        for i in range(min(len(a), len(b))):
            
            result = compare(a[i], b[i])

            # eventually when the recursion reaches 
            # a maximum point and It starts resolving, 
            # result will be something and the loop breaks
            if result == "left":
                return "left"
            elif result == "right":
                return "right"
        
        # special case, If both elements are equal
        if result == "equal":
            # the len() of the inputs need to be evaluated

            if len(a) < len(b):
                return("right")
            elif len(a) > len(b):
                return("left")
            else:
                return("equal")

    return result 
