def  partition(array, low, high):
    i = low-1
    pivot = array[high]
    for j in range(low, high):
        if array[j] < pivot:
            i+=1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[high] = array[high], array[i+1]
    return (i+1)

def quick_sort(array, low, high):
    if low<high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi-1)
        quick_sort(array, pi+1, high)

arr = [10, -11, 8, 9, 1, 5]
n = len(arr)
quick_sort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]),