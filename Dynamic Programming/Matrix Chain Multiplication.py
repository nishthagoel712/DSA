# p is the array which contain the order of matrices
def MCM(p):
    n=len(p)-1
    t=[[0 for i in range(n+1)]for j in range(n+1)]
    s=[[0 for i in range(n + 1)] for j in range(n + 1)]
    for l in range(2,n+1):
        for i in range(1,n-l+2):
            j=i+l-1
            t[i][j]=float("inf")
            for k in range(i,j):
                q=t[i][k]+t[k+1][j]+(p[i-1]*p[k]*p[j])
                if q<t[i][j]:
                    t[i][j]=q
                    s[i][j]=k
    return t[1][n],s
def printOrder(s,i,j):
    if i==j:
        print("A",i,end=" ")
    else:
        print("(",end=" ")
        printOrder(s,i,s[i][j])
        printOrder(s,s[i][j]+1,j)
        print(")",end=" ")
p=[5,10,3,12,5,50,6]
g,h=MCM(p)
print(g)
printOrder(h,1,len(p)-1)