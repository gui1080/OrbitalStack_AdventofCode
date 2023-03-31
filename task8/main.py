# --- Day 8: Treetop Tree House ---

# I'm using numpy here because It's considered faster
# Not sure how big the input could be, so Numpy is the way to go!
import numpy as np

# The part that turns the input into a matrix is in another file 
from aux.get_matrix import get_matrix_from_lines

# The code's input is in the "input.txt" file
input_file = open('input.txt', 'r')

# get all the lines in the input
Lines = input_file.readlines()

# turns input into integer 2D numpy matrix
myMap = np.array(get_matrix_from_lines(Lines))

# trees in the outer part of the map
# will be visible, automatically
nrows, ncolumns = np.shape(myMap)

visible = []
visible_spots = 0

# for every coordinate in my 2D map...
for iy, ix in np.ndindex(myMap.shape):

    '''
    "x elements" are visible by default
    "y elements" could be hidden

    xxxx <- visible
    xyyx
    xyyx
    xxxx <- visible
    ˆ  ˆ <- visible

    '''

    # edge trees
    if iy == 0 or ix == 0:
        visible_spots = visible_spots + 1

    elif ix == ncolumns-1 or iy == nrows-1:
        visible_spots = visible_spots + 1

    # middle trees
    elif iy != 0 and iy != nrows-1:

        if ix != 0 and ix != ncolumns-1:

            # at this point, there will always be
            # myMap[iy+1, ix] or myMap[iy, ix+1] 
            
            visible = []
            
            # look up
            # -----------

            print("Looking up!")

            for newY in range(0, iy):
    
                print("Comparing " + str(myMap[iy, ix]) + " and " + str(myMap[newY, ix]))
                    
                if myMap[iy, ix] > myMap[newY, ix]:
                    print("Visible!")

                else:
                    visible.append(False)
                    print("Not visible!")
                    break
            
            # look down
            # -----------
            
            print("Looking down!")

            for newY in range(iy+1, nrows):

                print("Comparing " + str(myMap[iy, ix]) + " and " + str(myMap[newY, ix]))
                        
                if myMap[iy, ix] > myMap[newY, ix]:
                    print("Visible!")

                else:
                        
                    visible.append(False)
                    print("Not visible!")
                    break

            # look to the left
            # -----------
            
            print("Looking to the left!")

            for newX in range(0, ix):
            
                print("Comparing " + str(myMap[iy, ix]) + " and " + str(myMap[iy, newX]))
                        
                if myMap[iy, ix] > myMap[iy, newX]:
                            
                    print("Visible!")

                else:

                    visible.append(False)
                    print("Not visible!")
                    break

            # look to the right
            # -----------
            
            print("Looking to the right!")

            for newX in range(ix+1, ncolumns):
        
                print("Comparing " + str(myMap[iy, ix]) + " and " + str(myMap[iy, newX]))
                        
                if myMap[iy, ix] > myMap[iy, newX]:
                            
                    print("Visible!")

                else:

                    visible.append(False)
                    print("Not visible!")
                    break

            if visible != [False, False, False, False]:
                
                visible.append([myMap[iy, ix], iy, ix])

                # new possible spot is available!
                visible_spots = visible_spots + 1


print("\n\nVisible spots - " + str(visible_spots) + "\n")