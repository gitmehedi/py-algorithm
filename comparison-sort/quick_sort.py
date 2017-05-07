"""
Quicksort is a divide and conquer algorithm which relies on a partition operation: to partition an array 
an element called a pivot is selected.[28][29] All elements smaller than the pivot are moved before it and 
all greater elements are moved after it. This can be done efficiently in linear time and in-place. 
The lesser and greater sublists are then recursively sorted. This yields average time complexity of 
O(n log n), with low overhead, and thus this is a popular algorithm. Efficient implementations of 
quicksort (with in-place partitioning) are typically unstable sorts and somewhat complex, but are 
among the fastest sorting algorithms in practice. Together with its modest O(log n) space usage, 
quicksort is one of the most popular sorting algorithms and is available in many standard programming libraries.

The important caveat about quicksort is that its worst-case performance is O(n2); while this is rare, 
in naive implementations (choosing the first or last element as pivot) this occurs for sorted data, 
which is a common case. The most complex issue in quicksort is thus choosing a good pivot element, 
as consistently poor choices of pivots can result in drastically slower O(n2) performance, but good 
choice of pivots yields O(n log n) performance, which is asymptotically optimal. For example, if at 
each step the median is chosen as the pivot then the algorithm works in O(n log n). Finding the median, 
such as by the median of medians selection algorithm is however an O(n) operation on unsorted lists and 
therefore exacts significant overhead with sorting. In practice choosing a random pivot almost certainly 
yields O(n log n) performance.

Time Complexity
================

Best Case: Theta(n log n)
Avg. Case: Omega(n log n)
Worst Case: BigOh(n*n)

"""


def partition(arr, left, right):
    i, j = left, right
    pivot = arr[(left+right)/2]
    
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    return i


def quick_sort(arr, left, right):
    index = partition(arr, left, right)
    if left < index-1:
        quick_sort(arr, left, index-1)
    if index < right:
        quick_sort(arr, index, right)
        
arr = [12, 5, 3, 4, 2, 89, 1, 65, 24, 15]
left, right = 0, len(arr)-1
quick_sort(arr, left, right)
print arr



