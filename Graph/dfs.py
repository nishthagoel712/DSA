from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def DFSUtil(self,v,visited):
        visited[v]=True
        print(v,end=" ")
        for i in self.graph[v]:
            if visited[i]==False:
                self.DFSUtil(i,visited)
    def DFS(self,s):
        visited=[False]*((len(self.graph))+1)
        self.DFSUtil(s,visited)
g = Graph()
g.addEdge(1,2)
g.addEdge(1,4)
g.addEdge(1,5)
g.addEdge(2,3)
g.addEdge(2,7)
g.addEdge(2,6)
g.addEdge(3,2)
g.addEdge(5,1)
g.addEdge(4,1)
g.addEdge(7,2)
g.addEdge(6,2)
print("Following is Breadth First Traversal"
      " (starting from vertex 1)")
g.DFS(1)