
from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        # Number of vertices
        self.V = vertices
        # defining default disctionary for the graph G.
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)


    def dfsAllPathUtil(self, u, v, visited, path):
        visited[u] = True
        path.append(u)
        if (u == v):
            print(path)

        else:
            for i in self.graph[u]:
                if (visited[i] == False):
                    self.dfsAllPathUtil(i,v, visited, path)



        path.pop()
        visited[u]= False

    def printAllPaths (self, u, v):

        visited = [False]*(self.V)
        path = []

        # Call the dfsAllPathUtil function to find all the path

        self.dfsAllPathUtil(u,v, visited, path)


g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(2, 0)
g.addEdge(2, 1)
g.addEdge(1, 3)

s = 2 ; d = 3
print ("Following are all different paths from %d to %d :" %(s, d))
g.printAllPaths(s, d)





