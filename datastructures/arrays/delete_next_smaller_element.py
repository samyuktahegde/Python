def delete_next_smaller_element(array, k):
    stack = []
    count = 0
    for i in range(0, len(array)):
        stack.append(array[i])
        print(stack)
        print('i', i)
        for j in range(i+1, len(array)):
            if len(stack)==0:
                break
            elif stack[-1]>array[j]:
                continue
            else:
                stack.pop()
                count+=1
        if count==k:
            break
    print(stack)

a = [3, 100, 1]
delete_next_smaller_element(a, 1)
        

