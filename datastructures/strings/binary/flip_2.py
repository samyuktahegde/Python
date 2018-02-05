def is_one_flip(string):
    sum = 0
    n = len(string)

    for c in string:
        sum += int(c)
    return(sum == n-1 or sum == 1)

result = 'Yes' if is_one_flip('1000000000001') else 'No'
print result