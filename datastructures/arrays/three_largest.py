from sys import maxint
def three_largest(array):
    first = -maxint-1
    second = -maxint-1
    third = -maxint-1
    for x in array:
        if x > first:
            third = second
            second = first
            first = x
        elif x > second:
            third = second
            second = x
        elif x > third:
            third = x
    print first, second, third

three_largest([1, 2, 3, 4])
            
