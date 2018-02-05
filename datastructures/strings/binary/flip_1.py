def can_make_all_same(string):
    zeroes = 0
    ones = 0
    for c in string:
        if c == '0': 
            zeroes += 1 
        else:
            ones += 1
    
    return (zeroes==1 or ones == 1)

result='Yes' if can_make_all_same('11000') else 'No'
print result
