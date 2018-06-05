def length_remaining(string_array):
    stack = []
    for s in string_array:
        if len(stack)==0:
            stack.append(s)
        else:
            if s==stack[-1]:
                stack.pop()
            else:
                stack.append(s)
    return len(stack)

string_array= ["tom", "jerry", "jerry", "tom"]
print(length_remaining(string_array))