# a is the Given array
def bitonicsubsequence(a):
    n=len(a)
    p=[1 for i in range(n)]
    g,b1=maxincsubsequence(a,n)
    b=a[::-1]
    h,y=maxincsubsequence(b,n)
    h=h[::-1]
    y=y[::-1]
    for i in range(n):
        p[i]=g[i]+h[i]-1
    maxi=max(p)
    k=p.index(maxi)
    q=b1[k]
    c=y[k][:len(y[k])-1]
    q.extend(sorted(c,reverse=True))
    return max(p)
def maxincsubsequence(a,n):
    t=[1 for i in range(n)]
    e=[[a[0]]]
    for i in range(1,n):
        f=[a[i]]
        for j in range(i):
            if a[j]<a[i]:
                if t[i]<t[j]+1:
                    t[i]=t[j]+1
                    f.append(a[j])
        e.append(sorted(f))
    return t,e
a=[2,-1,4,3,5,-1,3,2]
print(bitonicsubsequence(a))