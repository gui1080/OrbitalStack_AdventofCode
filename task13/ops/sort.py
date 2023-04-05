from ops.comparison import compare

# Good and old Bubble Sort
# But adapted for this structure
# In other words, using "compare()" 
# and not a basic integer comparison using ">" operator
def bubblue_sort(arr):
    
    n = len(arr)
    
    for i in range(n-1):

        swapped = False
        
        # last i elements are in place
        for j in range(0, n-i-1):

            # if arr[j] > arr[j+1]
            # swap! 
            if compare(arr[j], arr[j + 1]) == "left":

                swapped = True
                
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if swapped == False:

            break
