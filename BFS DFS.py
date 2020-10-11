class queue:
    def __init__(self, size):
        self.size = size
        self.data = [0 for i in range(self.size)]
        self.rear = 0
        self.front = 0

    def IsEmpty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    def enqueue(self, value):
        self.data[self.rear] = value
        self.rear = (self.rear + 1) % self.size

    def dequeue(self):
        x = self.data[self.front]
        self.front = (self.front + 1) % self.size
        return(x)


class stack:
    def __init__(self, size):
        self.size = size
        self.data = [0 for i in range(self.size)]
        self.top = 0

    def IsEmpty(self):
        #print('list is empty')
        if (self.top) == 0:
            return(True)
        else:
            return(False)

    def Push(self, value):
        if self.top != self.size:
            self.data[self.top] = value
            self.top = self.top + 1
            return(self.data)
        else:
            pass

    def pop(self):
        if self.top > -1:
            x = self.data[self.top - 1]
            self.top = self.top - 1
            return (x)
        else:
            return 'array is empty'

class Graph:
    def __init__(self,vertex):
        self.vertex = vertex
        self.array = [[0 for i in range(self.vertex)] for j in range(self.vertex)]

    def AddEdges(self,src,dest):
        if src == dest:
            print('same')
        else:
            self.array[src][dest] = 1
            self.array[dest][src] = 1

    def Print(self):
        for i in self.array:
            for j in i:
                print(j , end=' ')
            print()

    def GetNeighbour(self , vertex):
        a = []
        for i in range(len(self.array[vertex])):
            if self.array[vertex][i] == 1:
                a.append(i)
        return a

    def BFS(self,source):
        visit = []
        obj = queue(self.vertex)
        obj.enqueue(source)
        visit.append(source)
        while not obj.IsEmpty():
            z = obj.dequeue()
            print('visited ' , z)
            visit.append(z)
            nei = self.GetNeighbour(z)
            for i in nei:
                if i not in visit:
                    obj.enqueue(i)
                    visit.append(i)

    def DFS(self,source):
        visit = []
        obj = stack(self.vertex)
        obj.Push(source)
        visit.append(source)
        while not obj.IsEmpty():
            z = obj.pop()
            print('visited ' , z)
            visit.append(z)
            nei = self.GetNeighbour(z)
            for i in nei:
                if i not in visit:
                    obj.Push(i)
                    visit.append(i)





a = Graph(5)
a.AddEdges(1,2)
a.AddEdges(1,3)
a.AddEdges(2,4)
a.Print()
print('neighbours are ', a.GetNeighbour(1))
print('---------------------BFS---------------------')
a.BFS(1)
print('---------------------DFS---------------------')
a.DFS(1)