def bellman(l,source,n):
    dis=[float("inf") for i in range(n+1)]
    dis[source]=0
    for i in range(n-1):
        for e in l:
            u=e[0]
            v=e[1]
            c=e[2]
            if dis[u]+c<dis[v]:
                dis[v]=dis[u]+c
    return dis[1:]
n,m=map(int,input().split())
l=[]
for _ in range(m):
    a,b,wt=map(int,input().split())
    l.append([a,b,wt])
print(bellman(l,1,n))