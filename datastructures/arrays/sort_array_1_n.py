def sort_array(array):
    n = len(array)
    for i in range(n):
        array[i]=i+1
    return array

array = [1, 5, 3, 4, 2]
print(sort_array(array))