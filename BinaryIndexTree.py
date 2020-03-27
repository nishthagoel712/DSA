def getsum(BITtree,i):
    i=i+1
    s=0
    while i>0:
        s+=BITtree[i]
        i-=i&(-i)
    return s
def updatevalue(BITtree,i,value,n):
    i+=1
    while i<=n:
        BITtree[i]+=value
        i+=i&(-i)

def constTree(arr,n):
    BITtree=[0]*(n+1)
    for i in range(n):
        updatevalue(BITtree,i,arr[i],n)
    return BITtree

arr=[3,2,-1,6,5,4,-3,3,7,2,3]
BITtree=constTree(arr,len(arr))
print("sum of element in arr[0...5]",getsum(BITtree,5))
arr[3]+=3
updatevalue(BITtree,3,3,len(arr))
print("sum of element in arr[0...5] after updation",getsum(BITtree,5))

