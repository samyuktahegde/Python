def binomial_coeffient(n, k):
    c = [[0 for x in range(k+1)] for x in range(n+1)]

    for i in range(n+1):
        for j in range(min(i, k)+1):
            if j==0 or j==i:
                c[i][j] = 1
            else:
                c[i][j] = c[i-1][j-1]+c[i-1][j]
    return c[n][k]

n = 4
k = 2
print("Value of C[" + str(n) + "][" + str(k) + "] is " + str(binomial_coeffient(n,k)))
