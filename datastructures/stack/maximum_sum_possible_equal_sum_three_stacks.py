def max_sum(stack1, stack2, stack3):
    n1 = len(stack1)
    n2 = len(stack2)
    n3 = len(stack3)
    sum1 = sum(stack1)
    sum2 = sum(stack2)
    sum3 = sum(stack3)

    while(1):
        if n1==0 or n2==0 or n3==0:
            return 0
        if sum1==sum2 and sum2==sum3:
            return sum1
        
        if sum1>=sum2 and sum1>=sum3:
            stack1.pop()
            n1 = len(stack1)
            sum1 = sum(stack1)
        elif sum2>=sum1 and sum2>=sum3:
            stack2.pop()
            n2 = len(stack2)
            sum2 = sum(stack2)
        elif sum3>=sum1 and sum3>=sum2:
            stack3.pop()
            n2 = len(stack3)
            sum3 = sum(stack3)

stack1 = [3, 2, 1, 1, 1]
stack2 = [4, 3, 2]
stack3 = [2, 5, 4, 1]
print(max_sum(stack1, stack2, stack3))
                
            

