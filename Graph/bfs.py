from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def BFS(self,s):
        visited=[False]*((len(self.graph))+1)
        q=[]
        q.append(s)
        visited[s]=True
        while q:
            k=q.pop()
            print(k,end=" ")
            for i in self.graph[k]:
                if visited[i]==False:
                    q.append(i)
                    visited[i]=True
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
g.BFS(1)