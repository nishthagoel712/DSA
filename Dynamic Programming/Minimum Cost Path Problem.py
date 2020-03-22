# p is the given matrix
# n is the number of rows in a matrix
# m is the number of columns in each row of a matrix
def mincostpath(p,n,m):
    t=[[0 for i in range(m)]for j in range(n)]
    for i in range(n):
        for j in range(m):
            if i==0 and j==0:
                t[i][j]=p[i][j]
            elif i==0:
                t[i][j]=t[i][j-1]+p[i][j]
            elif j==0:
                t[i][j]=t[i-1][j]+p[i][j]
            else:
                t[i][j]=min(t[i-1][j],t[i][j-1])+p[i][j]
    return t[n-1][m-1]
p=[[1,3,5,8],[4,2,1,7],[4,3,2,3]]
n=3
m=4
print(mincostpath(p,n,m))
