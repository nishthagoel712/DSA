# l is the given sequence
# n is the nuber of element in a sequence
def longestincreasing(n,l):
    temp=[1 for i in range(n)]
    h=[]
    for i in range(0,n):
        j=0
        p=[l[i]]
        while j<i:
            if l[j]<l[i]:
                temp[i]=max(temp[i],temp[j]+1)
                if temp[i]==temp[j]+1 and len(p)<temp[j]+1:
                    p.append(l[j])
            j=j+1
        h.append(sorted(p))
    d=max(temp)
    c=temp.index(d)
    return d
n=7
l=[3,4,-1,0,6,2,3]
print(longestincreasing(n,l))
