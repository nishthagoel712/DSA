from collections import defaultdict
visited=defaultdict(bool)
stack=[]
def topological_sort_util(adj,vertex):
    visited[vertex]=True
    for node in adj[vertex]:
        if not visited[node]:
            topological_sort_util(adj,node)

    stack.append(vertex)

def topological_sort(adj):
    for vertex in adj:
        if not visited[vertex]:
            topological_sort_util(adj,vertex)

    return stack[::-1]


adj=defaultdict(list)
m=int(input())
for _ in range(m):
    a,b=input().split()
    adj[a].append(b)

print(*topological_sort(adj))