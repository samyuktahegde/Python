def get_odd_occurence(array):
    count_map = {}
    result = []
    for element in array:
        if element in count_map:
            count_map[element]+=1
        else:
            count_map[element] = 1
    print(count_map)
    for key, value in count_map.items():
        if value%2 != 0:
            result.append(key)
    return result

array = [2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2, 3]
print(get_odd_occurence(array))

