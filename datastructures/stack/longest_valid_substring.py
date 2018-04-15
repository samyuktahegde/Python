def find_max_length(string):
    n = len(string)
    stack = []
    stack.append(-1)

    result = 0
    for i in range(n):
        if string[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if len(stack) != 0:
                result = max(result, i-stack[len(stack)-1])
            else:
                stack.append(i)
    return result


string = "((()()"
print(find_max_length(string))
 
string = "()(()))))"
print(find_max_length(string))