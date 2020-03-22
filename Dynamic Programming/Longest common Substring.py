# x is the first string
# y is the second string
def lcs(x,y):
    n=len(x)
    m=len(y)
    p=[[0 for i in range(n+1)]for j in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                p[i][j]=0
            elif y[i-1]==x[j-1]:
                p[i][j]=p[i-1][j-1]+1
            else:
                p[i][j]=0
    maxi=float("-inf")
    for i in range(m+1):
        for j in range(n+1):
            if p[i][j]>maxi:
                maxi=p[i][j]
                a=i
                b=j
    return maxi

x="abcdaf"
y="zbcdf"
print(lcs(x,y))
