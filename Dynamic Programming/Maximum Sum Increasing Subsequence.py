# a is the given array
def suminc(a):
    n=len(a)
    t1=a[::]
    t2=[i for i in range(n)]
    for i in range(1,n):
        for j in range(0,i):
            if a[i]>=a[j]:
                k=t1[i]
                t1[i]=max(t1[i],t1[j]+a[i])
                if t1[i]!=k:
                    t2[i]=j
    return max(t1)
a=[2,3,8,4,6]
print(suminc(a))
