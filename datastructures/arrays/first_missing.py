def find_missing(array, start, end):
    if start>end:
        return end+1
    if (start != array[start]):
        return start
    mid = int((start+end)/2)
    print mid
    print array[mid]

    if (array[mid] == mid):
        return find_missing(array, mid+1, end)
    return find_missing(array, start, mid)

arr = [0, 1, 2, 3, 4, 5, 6, 8, 10]
n = len(arr)
print("Smallest missing element is",
      find_missing(arr, 0, n-1))