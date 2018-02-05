def check_divisibility(n, digit):
    return (digit != 0 and n%digit == 0)

def all_digits_divide(n):
    temp = n
    while temp>0:
        digit = temp%10
        if check_divisibility(n, digit) == False:
            return False
        temp = temp//10
    return True

n = 127
 
if (all_digits_divide(n)) :
    print("Yes")
else :
    print("No" )