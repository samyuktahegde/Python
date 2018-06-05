def generate_fibonacci_numbers(first, second, n):
    print(first)
    print(second)
    for i in range(0,n-2):
        sum = first+second
        print(sum)
        first=second
        second=sum


generate_fibonacci_numbers(5,8,5)
        