# n is the total number of jobs given
# jo contain starting and ending time of each job
# p is the profit related to each job
def job(n,p,jo):
    jo.sort(key=lambda x:x[1])
    l=p[::]
    for i in range(1,n):
        for j in range(0,i):
            if jo[j][1]<=jo[i][0]:
                l[i]=max(l[i],l[j]+p[i])
    return max(l)
n=6
p=[5,6,5,4,11,2]
jo=[(1,3),(4,6),(2,5),(6,7),(5,8),(7,9)]
print(job(n,p,jo))
