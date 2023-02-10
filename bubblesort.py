# Bubble sort

arr=[]
swapcount=0

# Getting input from the user
array=list(input("Enter the list to sort: ").split())
for i in array: arr.append(int(i))
'''
del array # Deleting the string array to save space 
'''
print(f"Given input: {arr}")

# The continuous loop to sort
while True:
    
    for i in range(len(arr)-1): #from 0 to n-1 (to avoid errors and check till n elements)
        if arr[i] > arr[i+1]:   
            # if val1>val2: swap (tuple assignment)
            (arr[i],arr[i+1])=(arr[i+1],arr[i])
            swapcount+=1       # No. of swaps
        else: continue  # if not greater, do not swap, go to next element
    
    # After completing one iteration, check if swapcount has not changed
    # i.e. if it has not changed (after checking) through the loop, then EXIT out of WHILE loop
    # if it has changed (incremented atleast by one), reassign as zero, continue loop
    
    else: # else part of FOR loop ('under' WHILE)
        if swapcount==0: break
        swapcount=0
        continue


print(f"Sorted array is {arr}")
    