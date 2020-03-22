# s is the given string
# d is the given dictionary of words
def string(s,d):
    l=len(s)
    m=[[False for i in range(l)]for j in range(l)]
    p=[[-1 for i in range(l)]for j in range(l)]
    for i in range(1,l+1):
        start=0
        end=i-1
        while end<l:
            a=s[start:end+1]
            if a in d:
                m[start][end]=True
            else:
                for k in range(start,end):
                    if m[start][k]==True and m[k+1][end]==True:
                        m[start][end]=True
                        p[start][end]=k
                        break
            start=start+1
            end=end+1
    return m[0][l-1]

d=['i','a','am','ace']
s='iamace'
print(string(s,d))

