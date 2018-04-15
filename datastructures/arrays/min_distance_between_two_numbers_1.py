def minimum_distance(array, n, x, y):
    min_distance = 999999999
    for i in range(n):
        for j in range(i+1, n):
            if (x==array[i] and y==array[j]) or (y==array[i] and x==array[j]) and min_distance>abs(i-j):
                min_distance = abs(i-j)
    return min_distance

arr = [3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3]
n = len(arr)
x = 3
y = 6
print("Minimum distance between ",x," and ",
     y,"is",minimum_distance(arr, n, x, y))