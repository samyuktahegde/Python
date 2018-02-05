def find_element(array, n, key):
    for i in range(n):
        if array[i] == key:
            return i
    return -1

arr = [12, 34, 10, 6, 40]
key = 40
n = len(arr)
  
#search operation
index = find_element(arr, n, key)
if index != -1:
    print ("element found at position: " + str(index + 1 )) 
else:
    print ("element not found")