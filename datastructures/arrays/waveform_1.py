def sort_in_wave(array, n):
    array.sort()
    for i in range(0, n-1, 2):
        array[i], array[i+1] = array[i+1], array[i]

arr = [10, 90, 49, 2, 1, 5, 23]
sort_in_wave(arr, len(arr))
for i in range(0,len(arr)):
    print arr[i], 