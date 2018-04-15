queue = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

stack = []

for i in range(0, len(queue)//2):
    stack.append(queue.pop())

while len(stack)>0:
    queue.insert(0, stack.pop())

for i in range(0, len(queue)//2):
    stack.append(queue.pop())

print(queue)
print(stack)

for i in range(0, len(queue)):
    print(stack.pop())
    print(queue.pop())

