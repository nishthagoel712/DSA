from collections  import defaultdict
from heapq import heapify,heappop,heappush
def dijikstra(v,n):
    e=[]   #priority queue
    heapify(e)
    heappush(e,[0,v])
    visited=[False for i in range(n+1)]
    min_dis=[float('inf') for i in range(n+1)]
    min_dis[v]=0
    while e:
        q=heappop(e)
        u=q[1]
        if visited[u]==False:
            visited[u]=True
            for w in adjacency[u]:
                if visited[w[1]]==False:
                    c=w[0]
                    v=w[1]
                    if min_dis[u]+c<min_dis[v]:
                        min_dis[v]=min_dis[u]+c
                        heappush(e,[min_dis[v],v])
    return min_dis[1:]
n,m=map(int,input().split())
adjacency=defaultdict(list)
for _ in range(m):
    a,b,wt=map(int,input().split())
    adjacency[a].append([wt,b])
print(dijikstra(1,n))