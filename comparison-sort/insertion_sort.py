"""
Insertion sort is a simple sorting algorithm that is relatively efficient for small lists and mostly sorted lists, 
and is often used as part of more sophisticated algorithms. It works by taking elements from the list one by one 
and inserting them in their correct position into a new sorted list.[19] In arrays, the new 
list and the remaining elements can share the array's space, but insertion is expensive, 
requiring shifting all following elements over by one. Shellsort (see below) is a variant of 
insertion sort that is more efficient for larger lists.

Time Complexity
================

Best Case: Theta(n)
Avg. Case: Omega(n*n)
Worst Case: BigOh(n*n)

"""


class InsertionSort(object):

    def __init__(self, lists):
        self.lists = lists
        self.len = len(self.lists)

    def sorting(self):
        for i in range(1, self.len):
            cur_val = self.lists[i]
            position = i
            while position>0 and self.lists[position-1] > cur_val :
                self.lists[position] = self.lists[position-1]
                position = position - 1
            self.lists[position] = cur_val

    def show_list(self):
        print "Insertion Sort Algorithm"
        print "========================"
        print self.lists


lists = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort = InsertionSort(lists)
insertion_sort.sorting()
insertion_sort.show_list()


