# arr represent given 2D matrix of 0's and 1's
# n is the number of rows in a matrix
# m is the number of columns in each row of a matrix
def rectangle(arr, n, m):
    maxi = float("-inf")
    temp = [0] * m
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                temp[j] = 0
            else:
                temp[j] += arr[i][j]
        w = histogram(temp)
        if w > maxi:
            maxi = w
    return maxi
def histogram(a):
    s = []
    maxarea = float("-inf")
    for j in range(len(a)):
        if len(s) < 1:
            s.append(j)
        elif a[j] >= a[s[-1]]:
            s.append(j)
        else:
            while len(s) > 0 and a[s[-1]] > a[j]:
                b = s.pop()
                if len(s) < 1:
                    area = a[b] * j
                    if area > maxarea:
                        maxarea = area
                else:
                    area = a[b] * (j - s[-1] - 1)
                    if area > maxarea:
                        maxarea = area

            s.append(j)
    j = j + 1
    while len(s) > 0:
        b = s.pop()
        if len(s) < 1:
            area = a[b] * j
            if area > maxarea:
                maxarea = area
        else:
            area = a[b] * (j - s[-1] - 1)
            if area > maxarea:
                maxarea = area
    return maxarea

n = 4
m = 6
arr = [[1, 0, 0, 1, 1, 1], [1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1]]
print(rectangle(arr, n, m))