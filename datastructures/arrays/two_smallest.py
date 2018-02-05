from sys import maxint
def print_two_smallest(array):
    first = maxint
    second = maxint
    for x in array:
        if x<first:
            second = first
            first = x
        elif x<second:
            second = x
    print first, second

print_two_smallest([1, 2, -3, -4])