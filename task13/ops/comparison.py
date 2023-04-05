
def compare(a, b):

    # one iteration from base case
    # the input will be two integers
    # ----------------------------------

    # if one element is a list
    # and the other is an integer
    if (type(a) == list) and (type(b) == int):
        result = compare(a, [b])
        return result

    elif (type(a) == int) and (type(b) == list):
        result = compare([a], b)
        return result

    # base case
    # ----------------------------------

    # If both elements are integers, nothing else to do
    # just compare
    elif (type(a) == int) and (type(b) == int):
        
        print("Comparing two integers")
        # recursion default case

        if a < b:
            return("right")
        elif a > b:
            return("left")
        elif a == b:
            return("equal")

    # ----------------------------------

    elif (type(a) == list) and (type(b) == list):
        
        print("Comparing two lists")

        result = "equal"

        for i in range(min(len(a), len(b))):
            
            result = compare(a[i], b[i])

            # eventually when the recursion reaches 
            # a maximum point and It starts resolving, 
            # result will be something and the for loop breaks
            if result == "right":
                return "right"
                #break
        
        # now we can evaluate "result" 
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
