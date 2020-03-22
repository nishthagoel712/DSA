# l is the length of given rod
# v is the array containing the price of rod at different length
def cuttingrod(l,v):
    p=[[0 for i in range(l+1)]for j in range(len(v)+1)]
    for i in range(len(v)+1):
        for j in range(l+1):
            if j>=i and i>0:
                p[i][j]=max(p[i-1][j],p[i][j-i]+v[i-1])
            else:
                p[i][j]=p[i-1][j]
    return p[len(v)][l]
l=8
v=[1,5,8,9,10,17,17,20]
print(cuttingrod(l,v))
