# str1 is the given string
def palindroepartition(str1):
    n=len(str1)
    t=[[0 for i in range(n)]for j in range(n)]
    for l in range(1,n+1):
        for i in range(n-l+1):
            j=i+l-1
            if ispalindrome(s[i:j+1]):
                t[i][j]=0
            else:
                t[i][j]=float("inf")
                for k in range(i,j):
                    q=1+t[i][k]+t[k+1][j]
                    if q<t[i][j]:
                        t[i][j]=q
    return t[0][n-1]
def ispalindrome(str2):
    if str2==str2[::-1]:
        return True
    return False
s="abcbm"
print(palindroepartition(s))