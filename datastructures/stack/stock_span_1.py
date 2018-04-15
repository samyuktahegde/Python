def calculate_span(price, n, S):
    S[0] = 1
    for i in range(1, n):
        S[i] = 1
        j = i-1
        while j>=0 and price[i]>=price[j]:
            S[i] += 1
            j -= 1

price = [10, 4, 5, 90, 120, 80]
n = len(price)
S = [None] * n

calculate_span(price, n, S)

print(S)
            
        
