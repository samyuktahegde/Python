def binary_search(array, l, r, x):
    while l<=r:
        mid = l + (r-l)/2
        if array[mid] == x:
            return mid
        elif array[mid]>x:
            r = mid -1
        else:
            l = mid+1
    return -1

array = [ 2, 3, 4, 10, 40 ]
x = 10
 
# Function call
result = binary_search(array, 0, len(array)-1, x)
 
if result != -1:
    print "Element is present at index %d" % result
else:
    print "Element is not present in array"
