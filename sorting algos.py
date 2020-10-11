import random


class sorting:
    def __init__(self, lst):
        self.lst = lst

    def GenerateRandom(self, n):
        for i in range(n):
            ran = random.randint(1, n)
            self.lst.append(ran)
        return self.lst

    def Printv(self):
        print('your list is', self.lst)

    def BubbleSort(self):
        i = 1
        n = len(self.lst)
        j = 1
        for i in range(n):
            for j in range(n - 1):
                if self.lst[j] > self.lst[j + 1]:
                    (self.lst[j], self.lst[j + 1]) = (self.lst[j + 1], self.lst[j])

        print('By Using Bubble Sort', self.lst)

    def insertionSort(self):
        for i in range(1, (len(self.lst))):
            key = self.lst[i]
            j = i - 1
            while j >= 0 and key < self.lst[j]:
                self.lst[j + 1] = self.lst[j]
                j = j - 1
            self.lst[j + 1] = key
        print('By Using Insertion Sort ', self.lst)

    def SelectionSort(self):

        for i in range(len(self.lst) - 1):
            m = i
            j = i + 1
            for j in range(i + 1, len(self.lst)):
                if self.lst[j] < self.lst[m]:
                    m = j

            if m != i:
                self.lst[m], self.lst[i] = self.lst[i], self.lst[m]
        print('By Using Selection Sort ', self.lst)

    def Search(self, value):
        j = 0
        i = 1
        while i < len(self.lst):
            if self.lst[i] < self.lst[i - 1]:
                j = 1
            i = i + 1
        if (not j):
            print('list is sorted ', self.lst)
            print('finding value By using binary search ')
            i = 1
            n = len(self.lst)
            j = n
            while i < j:
                m = (i + j) // 2
                if value > self.lst[m]:
                    i = m + 1
                else:
                    j = m
            if value == self.lst[i]:
                print('binary search')
                print('your value {} is on location {} '.format(value, i))
            else:
                print('value not found')

        else:
            print('List is not sorted', self.lst)
            print('sorting by using Bubble sort')
            self.BubbleSort()
            print('finding value by using binary search')
            i = 1
            n = len(self.lst)
            j = n
            while i < j:
                m = (i + j) // 2
                if value > self.lst[m]:
                    i = m + 1
                else:
                    j = m
            if value == self.lst[i]:
                print('binary search')
                print('your value {} is on location {} '.format(value, i))
            else:
                print('value not found')


a = []
b = []
c = []
d = [6, 2, 3, 4, 5]
sort = sorting(a)
sort.GenerateRandom(10)
sort.Printv()
sort.BubbleSort()
sort1 = sorting(b)
sort1.GenerateRandom(12)
sort1.Printv()
sort1.insertionSort()
sort2 = sorting(c)
sort2.GenerateRandom(13)
sort2.Printv()
sort2.SelectionSort()
sort3 = sorting(d)
sort3.Printv()
sort3.Search(4)
