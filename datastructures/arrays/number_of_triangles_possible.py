def num_of_triangles(array):
    n = len(array)
    array.sort()
    count = 0
    for i in range(0, n-2):
        k = i+2
        for j in range(i+1, n):
            while (k<n and array[i]+array[j]>array[k]):
                k+=1
            count+=k-j-1
    return count

arr = [10, 21, 22, 100, 101, 200, 300]
print(num_of_triangles(arr))