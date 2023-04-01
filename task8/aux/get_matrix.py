
def get_matrix_from_lines(DocLines):

    newMap = []
    newRow = []

    # for every line
    for line in DocLines:
        
        # for every char in line
        for char in line:
            
            # append as an integer
            if char != "\n":
                newRow.append(int(char))

        # append list of integers
        newMap.append(newRow)
        newRow = []

    return newMap