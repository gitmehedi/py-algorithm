"""
Merge sort takes advantage of the ease of merging already sorted lists into a new sorted list. 
It starts by comparing every two elements (i.e., 1 with 2, then 3 with 4...) and swapping them 
if the first should come after the second. It then merges each of the resulting lists of two 
into lists of four, then merges those lists of four, and so on; until at last two lists are merged 
into the final sorted list.[21] Of the algorithms described here, this is the first that scales well 
to very large lists, because its worst-case running time is O(n log n). It is also easily applied to 
lists, not only arrays, as it only requires sequential access, not random access. However, it has 
additional O(n) space complexity, and involves a large number of copies in simple implementations.

Merge sort has seen a relatively recent surge in popularity for practical implementations, 
due to its use in the sophisticated algorithm Timsort, which is used for the standard sort 
routine in the programming languages Python[22] and Java (as of JDK7[23]). Merge sort itself is 
the standard routine in Perl,[24] among others, and has been used in Java at least since 2000 in 
JDK1.3.[25][26]

Time Complexity
================

Best Case: Theta(n log n)
Avg. Case: Omega(n log n)
Worst Case: BigOh(n log n)

"""

import random


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)/2
        left_a = arr[:mid]
        right_a = arr[mid:]
         
        mergeSort(left_a)
        mergeSort(right_a)
         
        i,j,k = 0,0,0
         
        while(i<len(left_a) and j<len(right_a)):
            if left_a[i] < right_a[j]:
                arr[k] = left_a[i]
                i += 1
            else:
                arr[k] = right_a[j]
                j += 1
            k += 1
              
        while i < len(left_a):
            arr[k] = left_a[i]
            i += 1
            k += 1
        while j < len(right_a):
            arr[k] = right_a[j]
            j += 1
            k += 1
             

lists = [int(2516*random.random()) for i in xrange(10000)]
mergeSort(lists)
print lists
            
