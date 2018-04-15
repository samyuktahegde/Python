def minimum_distance(array, n, x, y):
    min_distance = 999999999
    for i in range(n):
        if array[i] == x or array[i] == y:
            prev = i
            break
    while i<n:
        if array[i] == x or array[i] == y:
            if array[prev] != array[i] and (i-prev) < min_distance:
                min_distance = i - prev
                prev = i
            else:
                prev = i
        i+=1
    return min_distance

           

arr = [3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3]
n = len(arr)
x = 3
y = 6
print("Minimum distance between ",x," and ",
     y,"is",minimum_distance(arr, n, x, y))