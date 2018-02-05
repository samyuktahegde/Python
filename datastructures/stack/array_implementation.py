from sys import maxsize

def create_stack():
    stack = []
    return stack

def is_empty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)
    print("pushed to stack " + item)

def pop(stack):
    if(is_empty(stack)):
        return (str(-maxsize-1))
    return stack.pop()

stack = create_stack()
push(stack, str(10))
push(stack, str(20))
push(stack, str(30))
print(pop(stack) + " popped from stack")