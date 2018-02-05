def merge(array, l, m, r):
    n1 = m-l+1
    n2 = r-m

    L = [0]*n1
    R = [0]*n2

    for i in range(n1):
        L[i] = array[l+i]

    for j in range(n2):
        R[j] = array[m+1+j]

    i=0
    j=0
    k=l

    while i<n1 and j<n2:
        if L[i]<=R[j]:
            array[k] = L[i]
            i+=1
        else:
            array[k] = R[j]
            j+=1
        k += 1

    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1
 
    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1

def merge_sort(array, l, r):
    if l<r:
        m = (l+(r-l)/2)
        merge_sort(array, l, m)
        merge_sort(array, m+1, r)
        merge(array, l, m ,r)

arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print ("Given array is")
for i in range(n):
    print ("%d" %arr[i]),
 
merge_sort(arr,0,n-1)
print ("\n\nSorted array is")
for i in range(n):
    print ("%d" %arr[i]),
