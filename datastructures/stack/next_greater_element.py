def next_greater_element(array):
    stack = []
    stack.append(array[0])
    for i in range(1, len(array)):
        