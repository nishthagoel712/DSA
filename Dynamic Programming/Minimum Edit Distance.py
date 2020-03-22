# x is the first string
# y is the second string
def minedit(x, y):
    n = len(x)
    m = len(y)
    p = [[0 for i in range(n + 1)] for j in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                p[i][j] = j
            elif j == 0:
                p[i][j] = i
            elif x[j - 1] != y[i - 1]:
                mini = min(p[i - 1][j], p[i][j - 1], p[i - 1][j - 1])
                p[i][j] = mini + 1
            else:
                p[i][j] = p[i - 1][j - 1]
    return p[m][n]



x = "azced"
y = "abcdef"
print(minedit(x, y))

