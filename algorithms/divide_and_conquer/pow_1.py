def power(x, y):
    if y==0:
        return 1
    elif y%2 == 0:
        return power(x, y/2)*power(x, y/2)
    else:
        return x*power(x, y/2)*power(x, y/2)

print power(2,3)