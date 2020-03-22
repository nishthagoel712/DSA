# s is the list of words
# l is the limit of no. of character in each line
def textjustification(s,l,w):
    c=[[0 for i in range(len(s))]for i in range(len(s))]
    for i in range(len(s)):
        for j in range(len(s)):
            if j>=i:
                k=l[i:j+1]
                d=sum(k)+(j-i)
                if d<=w:
                    c[i][j]=(w-d)**2
                else:
                    c[i][j]=-1
    t1=[0]*len(s)
    t2=[0]*len(s)
    for i in range(len(s)-1,-1,-1):
        j=len(s)-1
        if c[i][j]!=-1:
            t1[i]=c[i][j]
            t2[i]=j+1
        else:
            mini=float("inf")
            for j in range(len(s)-1,i,-1):
                if c[i][j-1]!=-1:
                    mini=min(mini,c[i][j-1]+t1[j])
                    if mini==c[i][j-1]+t1[j]:
                        y=j
            t1[i]=mini
            t2[i]=y
    return t1[0]
s=["manver","som","likes","to","code"]
l=[6,3,5,2,4]
w=10
print(textjustification(s,l,w))
