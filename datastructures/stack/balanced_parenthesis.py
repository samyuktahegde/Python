def balanced_parenthesis(input_string):   
    opening_braces = ['(', '{', '[']
    closing_braces = [')', '}', ']']
    matching_braces = {')':'(', '}':'{', ']':'['}
    stack_braces = []

    for i in range(len(input_string)):
        if input_string[i] in opening_braces:
            stack_braces.append(input_string[i])
        elif input_string[i] in closing_braces:
            if len(stack_braces)>0:
                if stack_braces[-1] == matching_braces[input_string[i]]:
                    stack_braces.pop()
            else:
                return False

    if len(stack_braces)>0:
        return False
    else:
        return True

print(balanced_parenthesis('[(])'))
