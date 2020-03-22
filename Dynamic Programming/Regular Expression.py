# t is the given text
# p is the given pattern
def regularexp(t,p):
    n=len(t)
    m=len(p)
    s=[[False for i in range(m+1)]for j in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i==0 and j==0:
                s[i][j]=True
            elif i==0:
                    if j<m:
                        if p[j-1]=='*' or p[j]=='*':
                            s[0][j]=True
                    elif j==m:
                        if p[j-1]=='*':
                            s[0][j]=True
            elif j==0:
                s[i][j]=False
            elif t[i-1]==p[j-1] or p[j-1]=='.':
                s[i][j]=s[i-1][j-1]
            elif p[j-1]=='*':
                if t[i-1]==p[j-2] or p[j-2]=='.':
                    s[i][j]=s[i-1][j]
                else:
                    s[i][j]=s[i][j-2]
            else:
                s[i][j]=False
    return s[n][m]
t= 'xaabyc'
p= 'xa*b.c'
print(regularexp(t,p))