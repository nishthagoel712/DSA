# l represent given 2D matrix
# n is the number of rows in a matrix
# m is the given nuber of column in each row
def maxsubrectangle(l,n,m):
    maxsum=float("-inf")
    start=[0]
    finish=[0]
    for left in range(m):
        temp=[0]*n
        for right in range(left,m):
            for i in range(n):
                temp[i]+=l[i][right]
            currentsum=kadans(temp,start,finish,n)
            if currentsum>maxsum:
                maxsum=currentsum
                finalright=right
                finalleft=left
                finalup=start[0]
                finaldown=finish[0]
    return maxsum
def kadans(a,start,finish,n):
    su=0
    maxsum=float("-inf")
    finish[0]=-1
    local_start=0
    for i in range(n):
        su+=a[i]
        if su<0:
            su=0
            local_start=i+1
        elif su>maxsum:
            maxsum=su
            start[0]=local_start
            finish[0]=i
    if finish[0]!=-1:
        return maxsum
    maxsum=a[0]
    start[0]=finish[0]=0
    for i in range(1,n):
        if a[i]>maxsum:
            maxsum=a[i]
            start[0]=finish[0]=i
    return maxsum
n=4
m=5
l=[[1,2,-1,-4,-20],[-8,-3,4,2,1],[3,8,10,1,3],[-4,-1,1,7,-6]]
k=maxsubrectangle(l,n,m)
print(k)