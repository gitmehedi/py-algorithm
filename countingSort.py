#!/bin/bash

def countSort(arr):
    outputArr = [0 for i in range(256)]
#     print "First Output Array: ", outputArr
    
    countArr = [0 for j in range(256)]
#     print "First Count Array: ", outputArr
    
    ans = ["" for _ in arr]
    print "First answer Array: ", ans
    
    for i in arr:
        countArr[ord(i)] +=1
    print "Last count Array: ", countArr
    
    for i in range(256):
        countArr[i] += countArr[i-1]
    print "Second Last count Array: ", countArr
 
    # Build the output character array
    for i in range(len(arr)):
        outputArr[countArr[ord(arr[i])]-1] = arr[i]
        countArr[ord(arr[i])] -= 1
    print "Second Last count Array: ", outputArr
    # contains sorted characters
    for i in range(len(arr)):
        ans[i] = outputArr[i]
    
    print "Second Last count Array: ", ans
    
    return ans 

# Driver program to test above function
arr = "kemonacho tumi ami val newi"
ans = countSort(arr)
print "Sorted character array is %s"  %("".join(ans))