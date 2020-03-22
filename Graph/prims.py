from collections import defaultdict
from heapq import heapify,heappop,heappush
def prims(v,n):
    min_cost=0
    e=[]   #priority queue
    heapify(e)
    heappush(e,[0,v])
    visited=[False for i in range(n)]
    while e:
        q=heappop(e)
        q1=q[1]
        if visited[q1]==False:
            visited[q1]=True
            min_cost+=q[0]
            for w in adjacency[q1]:
                if visited[w[1]]==False:
                    heappush(e,w)
    return min_cost
n,m=map(int,input().split())
adjacency=defaultdict(list)
for _ in range(m):
    a,b,wt=map(int,input().split())
    adjacency[a].append([wt,b])
    adjacency[b].append([wt,a])
print("minimum cost of spanning tree is ",prims(0,n))