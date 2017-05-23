"""
In computer science, counting sort is an algorithm for sorting a 
collection of objects according to keys that are small integers; that is, 
it is an integer sorting algorithm. It operates by counting the number of objects 
that have each distinct key value, and using arithmetic on those counts 
to determine the positions of each key value in the output sequence. 
Its running time is linear in the number of items and the difference between the 
maximum and minimum key values, so it is only suitable for direct use in situations 
where the variation in keys is not significantly greater than the number of items. 
However, it is often used as a subroutine in another sorting algorithm, radix sort, 
that can handle larger keys more efficiently. Because counting sort uses key values as 
indexes into an array, it is not a comparison sort, and the Omega(n log n) lower bound for 
comparison sorting does not apply to it.[1] Bucket sort may be used for many of the same 
tasks as counting sort, with a similar time analysis; however, compared to counting sort,
bucket sort requires linked lists, dynamic arrays or a large amount of preallocated memory 
to hold the sets of items within each bucket, whereas counting sort instead stores a single.

n = n is the number of input
k = k is the range of input
Time Complexity
================

Best Case: Theta(n+k)
Avg. Case: Omega(n+k)
Worst Case: BigOh(n+k)

"""


import random, string



class CountingSort(object):

    def __init__(self, lists):
        self.arr = lists
        self.len = 256
        self.outputArr = [0 for i in range(self.len)]
        self.countArr = [0 for j in range(self.len)]
        self.ans = ["" for _ in self.arr]

    def sorting(self):
        for i in self.arr:
            self.countArr[ord(i)] += 1

        for i in range(256):
            self.countArr[i] += self.countArr[i - 1]
        print self.countArr

        for i in range(len(self.arr)):
            self.outputArr[self.countArr[ord(self.arr[i])] - 1] = self.arr[i]
            self.countArr[ord(self.arr[i])] -= 1

    def show_list(self):
        print "Counting Sort Algorithm"
        print "========================"
        for i in range(len(self.arr)):
            self.ans[i] = self.outputArr[i]

        print "".join(self.ans)


# lists = ''.join([random.choice(string.ascii_letters + string.digits) for i in xrange(1000)])
lists = 'ABCDEFGHIJKLMOPQRSTUVWXYZabcdefghtjklmnopqrstuvwxyz012345dfadsfasdfasdfasdfasdfasdfasdfasdfasdfwerew2345234234234234236789'
counting_sort = CountingSort(lists)
counting_sort.sorting()
counting_sort.show_list()
