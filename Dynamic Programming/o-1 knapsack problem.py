# w is the weight array
# v is value array
# tw is total weight of knapsack
# ti is total item avaialable
def knapsack01(w,v,tw,ti):
    p=[[0 for i in range(tw+1)] for j in range(ti+1)]
    for j in range(1,tw+1):
        if w[0]<=j:
            p[1][j]=v[0]
    for i in range(2,ti+1):
        for j in range(1,tw+1):
            if w[i-1]>j:
                p[i][j]=p[i-1][j]
            else:
                p[i][j]=max(p[i-1][j],v[i-1]+p[i-1][j-w[i-1]])
    return p[ti][tw],p
def printknapsackitem(w,v,tw,ti,p):
    k=p[ti][tw]
    i=ti
    j=tw
    h=[]
    while i!=1:
        if k!=p[i-1][j]:
            h.append(w[i-1])
            i=i-1
            j=j-w[i]
        else:
            k=p[i-1][j]
            i=i-1
    return h
w=[1,3,4,5]
v=[1,4,5,7]
tw=7
ti=4
p,p1=knapsack01(w,v,tw,ti)
print(p)
h=printknapsackitem(w,v,tw,ti,p1)
print(h)