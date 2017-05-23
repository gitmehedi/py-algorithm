#!/bin/bash

def countSort(arr):
    outputArr = [0 for i in range(256)]
    countArr = [0 for j in range(256)]
    ans = ["" for _ in arr]
    
    for i in arr:
        countArr[ord(i)] +=1
        
    for i in range(256):
        countArr[i] += countArr[i-1]
    print countArr

    for i in range(len(arr)):
        outputArr[countArr[ord(arr[i])]-1] = arr[i]
        countArr[ord(arr[i])] -= 1

    for i in range(len(arr)):
        ans[i] = outputArr[i]
    
    return ans 

# Driver program to test above function
arr = "ABCDEFGHIJKLMOPQRSTUVWXYZabcdefghtjklmnopqrstuvwxyz0123456789"
ans = countSort(arr)
print "Sorted character array is %s"  %("".join(ans))