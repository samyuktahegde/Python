matrix = [[ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 1, 0 ]]

def celebrity(n):
    stack = []
    for i in range(0, n):
        stack.append(i)
    while len(stack)>1:
        a = stack.pop()
        b = stack.pop()
        if (knows(a=a,b=b)) is True:
            stack.append(b)
        else:
            stack.append(a)
    c = stack.pop()

    for i in range(0, n):
        if i!=c and knows(a=c,b=i) and (not knows(a=i,b=c)):
            return -1
    return c

def knows(a, b, matrix=matrix):
    return matrix[a][b]==1
    

n = 4
print(celebrity(n))


