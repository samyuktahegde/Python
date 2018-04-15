def first_even_occurence(array):
    count_map = {}
    for n in array:
        if n in count_map:
            count_map[n]= not count_map[n]
            if count_map[n] is True:
                return n
        else:
            count_map[n] = False
    return 0

# a = [1, 5, 4, 7, 4, 1, 5, 7, 1, 5]
# print(first_even_occurence(a))

a = [2, 4, 6, 8, 1, 6]
print(first_even_occurence(a))