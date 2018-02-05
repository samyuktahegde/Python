def print_ge(array):
    for i in range(0, len(array), 1):
        next = -1
        for j in range(i+1, len(array), 1):
            if array[i] < array[j]:
                next = array[j]
                break
        print str(array[i])+' --- '+str(next)

array = [11,13,21,3]
print_ge(array)