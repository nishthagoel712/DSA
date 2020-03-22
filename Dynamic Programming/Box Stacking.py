# arr contain l,b,h of different boxes
# n is the nuber of boxes given
def boxstacking(arr, n):
    k = [[0, 0, 0] for i in range(3 * n)]
    area = [0 for i in range(3 * n)]

    p = [i for i in range(3 * n)]
    j = 0
    for i in range(n):
        k[j][2] = arr[i][2]
        k[j][0] = max(arr[i][0], arr[i][1])
        k[j][1] = min(arr[i][0], arr[i][1])
        j = j + 1
        k[j][2] = arr[i][1]
        k[j][0] = max(arr[i][0], arr[i][2])
        k[j][1] = min(arr[i][0], arr[i][2])
        j = j + 1
        k[j][2] = arr[i][0]
        k[j][0] = max(arr[i][1], arr[i][2])
        k[j][1] = min(arr[i][1], arr[i][2])
        j = j + 1

    for i in range(3 * n):
        area[i] = k[i][0] * k[i][1]
    k.sort(key=lambda x: x[0] * x[1], reverse=True)
    t = [k[i][2] for i in range(3 * n)]
    for i in range(1, 3 * n):
        for j in range(i):
            if k[i][0] < k[j][0] and k[i][1] < k[j][1]:
                t[i] = t[j] + k[i][2]
                p[i] = j
    return max(t)
arr = [[4, 6, 7], [1, 2, 3], [4, 5, 6], [10, 12, 32]]
n = 4
print(boxstacking(arr, n))

