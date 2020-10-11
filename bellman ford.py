class graph:
    def __init__(self,vertex):
        self.vertex = vertex
        self.graph = []

    def AddEdges(self,src,dest, cost):
        if src == dest:
            print('same')
        else:
            self.graph.append([src,dest,cost])

    def Print(self,distance):
        for i in range(self.vertex):
            print('distance is ' , distance[i])

    def Bellman(self,src):
        distance = [999999 for i in range(self.vertex)]
        distance[src] = 0

        for i in range(self.vertex - 1):
            for u,v,w in self.graph:
                if distance[u] != 999999 and distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w

        for u,v,w in self.graph:
            if distance[u] != 999999 and distance[u] + w < distance[v]:
                print('contain negative cycle')
                return

        self.Print(distance)


g = graph(5)
g.AddEdges(0, 1, -1)
g.AddEdges(0, 2, 4)
g.AddEdges(1, 2, 3)
g.AddEdges(1, 3, 2)
g.AddEdges(1, 4, 2)
g.AddEdges(3, 2, 5)
g.AddEdges(3, 1, 1)
g.AddEdges(4, 3, -3)
g.Bellman(0)

