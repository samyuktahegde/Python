def print_leaders(array):
    size = len(array)
    max_from_right = array[-1]
    print(max_from_right)
    for i in range(size-1, -1, -1):
        if max_from_right<array[i]:
            max_from_right = array[i]
            print(array[i])

array = [16, 17, 4, 3, 5, 2]
print_leaders(array)
