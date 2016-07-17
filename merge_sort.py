#!/bin/bash

def mergeSort(alist):
    
    print "Splitting", alist
    
    if len(alist)>1:
        mid = len(alist)/2
        lefthalf= alist[:mid]
        righthalf= alist[mid:]
        
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i,j,k=0,0,0
        
        while i<len(lefthalf) and j< len(righthalf):
            
            
            if lefthalf[i]< righthalf[j]:
                alist[k]=lefthalf[j]
                i+=i
            else:
                alist[k] = righthalf[j]
                i+=i
                j+=j
                                
        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i+=i
            k+=k
        
        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i+=i
            k+=k


alist = [54,26,93,17,77,31,44,55,20]
print "Merging", alist
mergeSort(alist)
print(alist)