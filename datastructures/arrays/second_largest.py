from sys import maxint
def second_largest(array):
    first = -maxint-1
    second = -maxint-1
    for i in range(len(array)):
        if array[i] > first:
            second = first
            first = array[i]
        elif array[i]<first and array[i]>second:
            second = array[i]

    return second

array = [1, 2, 5, 6, 7, 7]
print second_largest(array)

