def reverse_a_number(number):
    stack = []
    n = number
    while n!=0:
        remainder = n%10
        n = n//10
        stack.append(remainder)
    reverse = 0
    while len(stack)>0:
        reverse = reverse*10 + stack.pop(0)
    return reverse
        
        

print(reverse_a_number(1234))