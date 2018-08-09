def find_element(array, input):
    n = len(array)
    if array[0]==input:
        return 0
    for i in range(1, n):
        if array[i]==input:
            return i
        else:
            if array[i-1]<input and input<array[i] and array[i-1]<array[i]:
                return i-1
            else:
                if array[i-1]>input and array[i]>input and array[i-1]>array[i]:
                    return -1

array=[23, 25, 33, 46, 52, 10, 13, 16, 20]
input = 5
print(find_element(array, input))
