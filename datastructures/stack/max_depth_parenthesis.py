def max_depth(S):
    current_max = 0
    max = 0
    n = len(S)

    for i in range(0, n):
        if S[i] == '(':
            current_max+=1
            if current_max>max:
                max = current_max
        elif S[i] == ')':
            if current_max>0:
                current_max-=1
            else:
                return -1
    if current_max != 0:
        return -1
    return max

s = "( ((X)) (((Y))) )"
print (max_depth(s))
        