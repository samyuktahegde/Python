def sort_stack(array):
    temp_stack = []
    while len(array)>0:
        temp = array.pop()
        if len(temp_stack)>0:
            if temp > temp_stack[-1]:
                temp_stack.append(temp)
            else:
                while len(temp_stack)>0 and temp_stack[-1]>temp:
                    array.append(temp_stack.pop())
                temp_stack.append(temp)
        else:
            temp_stack.append(temp)
    print(temp_stack)

array = [34, 3, 31, 98, 92, 23]
sort_stack(array)


            
