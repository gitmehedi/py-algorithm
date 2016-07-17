#!/bin/bash

def partition(arr,left,right):
    i,j=left,right
    temp
    pivot = arr[(left+right)/2]
    
    while(i<=j):
        while(arr[i]<pivot):
            i=i+1
        while(arr[j] > pivot):
            j=j-1
        if(i<=j):
            tmp = arr
            arr[i]=arr[j]
            arr[i]=arr[j]
            i=i+1
            j=j+1
            
    return i

def quickSort(arr,left,right):
    index = partition(arr,left,right)
    if(left<index-1):
        quickSort(arr,left,right-1)
    if(index<right):
        quickSort(arr,index,right)
        

