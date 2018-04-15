def smallest_greater(array):
    sorted_array = array[:]
    sorted_array.sort()
    outer_array=[]
    for i in range(0, len(sorted_array)):
        index = sorted_array.index(array[i])
        if index<len(sorted_array)-1:
            outer_array.append(sorted_array[index+1])
        else:
            outer_array.append('_')
    print(outer_array)

a = [6, 3, 9, 8, 10, 2, 1, 15, 7]
smallest_greater(a)
