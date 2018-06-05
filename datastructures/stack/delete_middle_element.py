# def delete_mid(stack, n, current):
#     if len(stack)==0 or current<n:
#         return
#     x = stack.pop()
#     delete_mid(stack, n, current+1)
#     if current!=n//2:
#         stack.append(x)

def delete_mid(stack, n, current):
    if len(stack)!=0 or current<n:
        x = stack.pop()
        delete_mid(stack, n, current+1)
        stack.append(x)
    if len(stack)!=0 and current==n//2:
        stack.pop()

stack = [1,2,3,4,5,6]
delete_mid(stack, len(stack), 0)
print(stack)
    