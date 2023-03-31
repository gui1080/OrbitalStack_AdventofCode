
def get_matrix_from_lines(DocLines):

    newMap = []
    newRow = []

    for line in DocLines:
        
        for char in line:
            
            if char != "\n":
                newRow.append(int(char))

        newMap.append(newRow)
        newRow = []

    return newMap