#!/bin/bash
import random

def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)/2
        leftA = arr[:mid]
        rightA = arr[mid:]
         
        mergeSort(leftA)
        mergeSort(rightA)
         
        i,j,k = 0,0,0
         
        while(i<len(leftA) and j<len(rightA)):
            if leftA[i]<rightA[j]:
                arr[k]=leftA[i]
                i +=1
            else:
                arr[k]=rightA[j]
                j +=1
            k +=1   
              
        while i<len(leftA):
            arr[k]=leftA[i]
            i +=1
            k +=1
        while j<len(rightA):
            arr[k]=rightA[j]
            j +=1
            k +=1
             
             
             
arr = [int(2516*random.random()) for i in xrange(10000)]
# arr = [54,26,93,17,77,31,44,55,20]
 
mergeSort(arr)
print arr
            
            
# def mergeSort(alist):
#      
#     if len(alist)>1:
#         mid = len(alist)/2
#         lefthalf= alist[:mid]
#         righthalf= alist[mid:]
#          
#         mergeSort(lefthalf)
#         mergeSort(righthalf)
#         i,j,k=0,0,0
#          
#         while i<len(lefthalf) and j< len(righthalf):
#              
#             if lefthalf[i]< righthalf[j]:
#                 alist[k]=lefthalf[i]
#                 i +=1
#             else:
#                 alist[k] = righthalf[j]
#                 j +=1
#              
#             k +=1
#                                  
#         while i < len(lefthalf):
#             alist[k]=lefthalf[i]
#             i +=1
#             k +=1
#          
#         while j < len(righthalf):
#             alist[k]=righthalf[j]
#             j +=1
#             k +=1
#  
#  
# alist = [54,26,93,17,77,31,44,55,20]
# alist = [int(10000*random.random()) for i in xrange(10000)]
# # print "Merging", alist
# mergeSort(alist)
# print(alist)