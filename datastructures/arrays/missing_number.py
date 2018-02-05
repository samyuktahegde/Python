def get_missing_number(array):
    n = len(array)
    total=(n+1)*(n+2)/2
    array_sum = sum(array)
    return total-array_sum

A = [1, 2, 4, 5, 6]
print(get_missing_number(A))