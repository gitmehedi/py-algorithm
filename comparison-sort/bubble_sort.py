"""
Bubble sort is a simple sorting algorithm. The algorithm starts at the beginning of the data set. 
It compares the first two elements, and if the first is greater than the second, it swaps them. 
It continues doing this for each pair of adjacent elements to the end of the data set. 
It then starts again with the first two elements, repeating until no swaps have occurred on the last pass.
This algorithm's average time and worst-case performance is O(n2), so it is rarely used to sort large, 
unordered data sets. Bubble sort can be used to sort a small number of items (where its asymptotic 
inefficiency is not a high penalty). Bubble sort can also be used efficiently 
on a list of any length that is nearly sorted 
(that is, the elements are not significantly out of place). 
For example, if any number of elements are out of place by only 
one position (e.g. 0123546789 and 1032547698), bubble sort's exchange will get them in order on the first pass, 
the second pass will find all elements in order, so the sort will take only 2n time.

Time Complexity
================

Best Case: Theta(n)
Avg. Case: Omega(n*n)
Worst Case: BigOh(n*n)

"""


class BubbleSort(object):

    def __init__(self, lists):
        self.lists = lists
        self.len = len(self.lists)

    def sorting(self):
        for i in range(self.len-1, 0, -1):
            for j in range(i):
                if self.lists[j] > self.lists[j+1]:
                    temp = self.lists[j]
                    self.lists[j] = self.lists[j+1]
                    self.lists[j+1] = temp

    def show_list(self):
        print lists

lists = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort = BubbleSort(lists)
bubble_sort.sorting()
bubble_sort.show_list()

