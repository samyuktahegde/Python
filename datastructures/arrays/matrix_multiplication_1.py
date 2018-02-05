def multiply(a, b):
    n = len(a[0])
    print n
    c = [[None]*n for i in range(n)]
    print c[0][0]
    for i in range(n):
        for j in range(n):
            c[i][j] = 0
            for k in range(n):
                c[i][j] = a[i][k]*b[k][j]
    return c

a = [{1, 2}]
b = [{1, 2}]
multiply(a, b)