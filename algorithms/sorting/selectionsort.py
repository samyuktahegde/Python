import sys

def selectionsort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[min_index]>array[j]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]
    return array

A = [22, 66, 11, 77, 10, 88]
print selectionsort(A)