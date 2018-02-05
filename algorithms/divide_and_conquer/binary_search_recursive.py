def binary_search(array, l, r, x):
    if r >= l:
        mid = l + (r-l)/2

        if array[mid] == x:
            return mid
        elif array[mid] > x:
            return binary_search(array, l, mid-1, x)
        else:
            return binary_search(array, mid+1, r, x)
    else:
        return -1

# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 40
 
# Function call
result = binary_search(arr, 0, len(arr)-1, x)
 
if result != -1:
    print "Element is present at index %d" % result
else:
    print "Element is not present in array"

