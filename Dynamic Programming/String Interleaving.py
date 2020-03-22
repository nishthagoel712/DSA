# s1 is the first String
# s2 is the second String
# s3 is the third String
def interleaving(s1,s2,s3):
    s1=' '+s1
    s2=' '+s2
    s3=' '+s3
    n=len(s1)
    m=len(s2)
    t=[[True for i in range(n)]for i in range(m)]
    for i in range(m):
        k=i
        for j in range(n):
            if i==0 and j==0:
                t[i][j]=True
            elif s3[k]==s1[j] or s3[k]==s2[i]:
                if s3[k]==s1[j]:
                    t[i][j]=t[i][j-1]
                elif s3[k]==s2[i]:
                    t[i][j]=t[i-1][j]
            else:
                t[i][j]=False
            k=k+1
    return t[m-1][n-1]
s1="aab"
s2="axy"
s3="aaxaby"
print(interleaving(s1,s2,s3))