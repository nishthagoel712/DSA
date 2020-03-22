# s is the given String
def lps(s):
    l=len(s)
    p=[[0 for i in range(l)]for j in range(l)]
    for i in range(1,l+1):
        start=0
        end=i-1
        while end<l:
            if i==1:
                p[start][end]=1
            elif s[start]==s[end]:
                p[start][end]=p[start+1][end-1]+2
            else:
                p[start][end]=max(p[start+1][end],p[start][end-1])
            start=start+1
            end=start+(i-1)
    return p[0][l-1]
s="fcgf"
print(lps(s))
