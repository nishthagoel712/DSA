# f is the number of given floors
# e is the number of given egg
def eggdropping(f,e):
    p=[[0 for i in range(f+1)]for j in range(e+1)]
    for i in range(1,e+1):
        for j in range(1,f+1):
            if i==1:
                p[i][j]=j
            elif j<i:
                p[i][j]=p[i-1][j]
            else:
                p[i][j]=float("inf")
                for k in range(1,j+1):
                    q=1+max(p[i-1][k-1],p[i][j-k])
                    if q<p[i][j]:
                        p[i][j]=q
    return p[e][f]
e=3
f=4
print(eggdropping(f,e))