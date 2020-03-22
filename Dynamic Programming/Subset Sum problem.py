# s is the given sum
# n is the total number of non-negative integer in a set
# l is the set of non-negative integer
def issubsetsum(s,l,n):
    p=[[False for i in range(s+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(s+1):
            if j==0:
                p[i][j]=True
            elif j<l[i-1] and j>0:
                p[i][j]=p[i-1][j]
            else:
                p[i][j]=p[i-1][j] or p[i-1][j-l[i-1]]
    return p[n][s]

print(issubsetsum(20,[3,7,8,9,10],5))

