# p is the given 2D matrix
# n is the number of rows in a matrix
# m is the number of columns in each row of a matrix
def maxsubsquare(p,n,m):
    t=[[0 for i in range(m+1)]for j in range(n+1)]
    maxi=float("-inf")
    for i in range(1,n+1):
        for j in range(1,m+1):
            if p[i-1][j-1]==0:
                t[i][j]=0
                maxi=max(maxi,t[i][j])
            else:
                t[i][j]=min(t[i-1][j-1],t[i-1][j],t[i][j-1])+1
                maxi=max(maxi,t[i][j])
    return maxi
p=[[0,0,1,1,1],[1,0,1,1,1],[0,1,1,1,1],[1,0,1,1,1]]
n=4
m=5
print(maxsubsquare(p,n,m))
