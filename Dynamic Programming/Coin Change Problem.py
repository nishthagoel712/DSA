# c is the array of available coins
# t is the total
# n is the total nuber of coins available
def coinchange(c,t,n):
    p=[[0 for i in range(t+1)]for j in range(n)]
    for i in range(n):
        p[i][0]=1
    for i in range(n):
        for j in range(1,t+1):
            if j<c[i]:
                p[i][j]=p[i-1][j]
            else:
                p[i][j]=p[i-1][j]+p[i][j-c[i]]
    return p[n-1][t]
c=[1,2,3]
t=5
n=len(c)
print(coinchange(c,t,n))