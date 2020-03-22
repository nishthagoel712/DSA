# x is the first string
# y is the second string
def LCS(x,y):
    n=len(x)
    m=len(y)
    p=[[0 for i in range(m+1)]for j in range(n+1)]
    t=[[0 for i in range(m + 1)]for j in range(n + 1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if x[i-1]==y[j-1]:
                p[i][j]=p[i-1][j-1]+1
                t[i][j]="diagonal"
            else:
                if p[i-1][j]>=p[i][j-1]:
                    p[i][j] = p[i - 1][j]
                    t[i][j] = "up"
                else:
                    p[i][j] = p[i][j - 1]
                    t[i][j] = 'left'
    return p[n][m]
x="ABCBDAB"
y="BDCABA"
print(LCS(x,y))
