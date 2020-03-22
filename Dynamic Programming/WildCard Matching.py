# p is the pattern given
# s is the string given
def wildcard(p,s):
    m=len(p)
    n=len(s)
    p=' '+p
    s=' '+s
    t=[[False for i in range(m+1)]for j in range(n+1)]
    flag=0
    for i in range(n+1):
        for j in range(m+1):
            if i==0 and j==0:
                t[i][j]=True
            elif i==0 and p[j]=='*' and flag==0:
                t[i][j]=True
            elif i==0 or j==0:
                t[i][j]=False
                flag=1
            else:
                if s[i]==p[j] or p[j]=='?':
                    t[i][j]=t[i-1][j-1]
                elif p[j]=='*':
                    t[i][j]=t[i-1][j] or t[i][j-1]
                else:
                    t[i][j]=False
    return t[n][m]
p='x?y*z'
s="xaylmz"
print(wildcard(p,s))
