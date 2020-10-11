class Stack:
    def __init__(self,size):
        self.size = size
        self.data = [0 for i  in range(self.size)]
        self.top = 0

    def IsEmpty(self):
        if self.top == 0:
            return True
        else:
            return False

    def Push(self,value):
        if self.top != self.size:
            self.data[self.top] = value
            self.top = self.top + 1
            return self.data
        else:
            return 'stack over flow'

    def Pop(self):
        if self.top > -1:
            x = self.data[self.top-1]
            self.top = self.top - 1
            return (x)
        else:
            return 'array is empty'

    def Count(self):
        n = len(self.data)
        print('total elements in stack ' , n)


    def Print(self):
        for i in (self.data):
            print(i)


a = Stack(5)
print(a.IsEmpty())
a.Push(1)
a.Push(2)
a.Push(3)
a.Push(4)
a.Push(5)
print('print stack')
a.Print()
print(' pop elements')
print(a.Pop())
#print(a.Pop())
a.Count()

