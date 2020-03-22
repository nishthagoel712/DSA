# a is the given array
def jump(a):
    n=len(a)
    t1=[float("inf")]*n
    t2=[-1]*n
    t1[0]=0
    for i in range(1,n):
        for j in range(0,i):
            if i<=j+a[j]:
                k=t1[i]
                t1[i]=min(t1[i],t1[j]+1)
                if t1[i]!=k:
                    t2[i]=j
    return t1[len(a)-1]
a=[2,3,1,1,2,4,2,0,1,1]
print(jump(a))

