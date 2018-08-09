def find_non_duplicates(array):
    n = len(array)
    m = n
    k = 1
    if array[0] == array[n-1]:
        k = 2
        m = n-1

    while k<m:
        if array[k]==array[k-1]:
            k+=2
        else:
            print(array[k-1])

find_non_duplicates([7, 7, 8, 8, 9, 1, 1, 4, 2, 2 ])
    