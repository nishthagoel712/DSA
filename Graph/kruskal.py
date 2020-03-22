def root(a):
    while parent[a] != a:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a

def union(a, b):
    root_a = root(a)
    root_b = root(b)
    if root_a!=root_b:
        if size[root_a] <= size[root_b]:
            parent[root_a] = root_b
            size[root_b] += size[root_a]
            size[root_a] = 0
        else:
            parent[root_b] = root_a
            size[root_a] += size[root_b]
            size[root_b] = 0


def kruskal(edges):
    min_cost = 0
    for e in edges:
        a = e[1][0]
        b = e[1][1]
        wt = e[0]
        if root(a) != root(b):
            union(a, b)
            min_cost += wt
    return min_cost


n, m = map(int, input().split())
size=[1 for i in range(n+1)]
parent=[i for i in range(n+1)]
edges= []
for _ in range(m):
    a, b, wt = map(int, input().split())
    edges.append([wt, (a, b)])
edges.sort()
print("minimum weight of spanning tree is",kruskal(edges))