def floyd(a):
    n=len(a)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                a[i][j]=min(a[i][j],a[i][k]+a[k][j])
    return a
INF=float('inf')
graph=[[0,5,INF,10],
       [INF,0,3,INF],
       [INF,INF,0,1],
       [INF,INF,INF,0]]
print(floyd(graph))