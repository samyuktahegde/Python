import math as m

def sum_of_factors(n):
    res = 1
    for i in range(2, int(m.sqrt(n)+1)):
        # count = 0
        current_sum = 1
        current_term = 1

        while n%i == 0:
            # count = count+1
            n /= i

            current_term *= i
            current_sum += current_term
        res *= current_sum
    if n > 2:
        res *= (1+n)
    return res

sum = sum_of_factors(30)
print ("Sum of all divisors is: ",sum)
