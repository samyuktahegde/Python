fibarray = [0, 1]

def fibonacci(n):
    if n<0:
        print "Incorrect Input"
    elif n<=len(fibarray):
        return fibarray[n-1]
    else:
        temp_fib = fibonacci(n-1)+fibonacci(n-2)
        fibarray.append(temp_fib)
        return temp_fib

print fibonacci(9)