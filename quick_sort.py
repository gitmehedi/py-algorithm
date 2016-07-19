#!/bin/bash

# define and explain partition of quicksort algortim

def partition(arr,left,right):
    i,j=left,right
    pivot=arr[(left+right)/2]
    
    while(i<=j):
        while(arr[i]<pivot):
            i +=1
        while(arr[j]>pivot):
            j -=1
        if(i<=j):
            arr[i],arr[j] = arr[j],arr[i]
            i +=1
            j -=1
    return i

def quickSort(arr,left,right):
    index = partition(arr,left,right)
    if(left<index-1):
        quickSort(arr,left,index-1)
    if(index<right):
        quickSort(arr,index,right)
        
arr = [12,5,3,4,2,89,1,65,24,15]   
left,right = 0,len(arr)-1
quickSort(arr,left,right)
print arr

# def partition(arr,left,right):
#     i,j=left,right
#     pivot = arr[(left+right)/2]
#     
#     while(i<=j):
#         while(arr[i]<pivot):
#             i=i+1
#         while(arr[j] > pivot):
#             j=j-1
#         if(i<=j):
#             arr[i],arr[j]=arr[j],arr[i]
#             i +=i
#             j -=1
#             
#     return i
# 
# def quickSort(arr,left,right):
#     index = partition(arr,left,right)
#     if(left<index-1):
#         quickSort(arr,left,right-1)
#     if(index<right):
#         quickSort(arr,index,right)
#         
# arr = [12,5,3,4,2,89,1,65,24,15]
# left = 0
# right = len(arr)-1
# quickSort(arr,left,right)
# print "Sorted array is: ", arr


