"""
Selection sort is an in-place comparison sort. It has O(n2) complexity, making it inefficient on large lists,
and generally performs worse than the similar insertion sort. Selection sort is noted for its simplicity, and 
also has performance advantages over more complicated algorithms in certain situations.

The algorithm finds the minimum value, swaps it with the value in the first position, and repeats these 
steps for the remainder of the list.[20] It does no more than n swaps, and 
thus is useful where swapping is very expensive.

Time Complexity
================

Best Case: Theta(n*n)
Avg. Case: Omega(n*n)
Worst Case: BigOh(n*n)

"""


class SelectionSort(object):

    def __init__(self, lists):
        self.lists = lists
        self.len = len(self.lists)

    def sorting(self):
        for i in range(self.len-1, 0, -1):
            positionOfMax = 0
            for j in range(1, i+1):
                if self.lists[j] > self.lists[positionOfMax]:
                    positionOfMax = j

            temp = self.lists[positionOfMax]
            self.lists[positionOfMax] = self.lists[i]
            self.lists[i] = temp

    def show_list(self):
        print "Insertion Sort Algorithm"
        print "========================"
        print self.lists


lists = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort = SelectionSort(lists)
selection_sort.sorting()
selection_sort.show_list()


