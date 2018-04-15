def reverse(queue, k):
    stack = []
    for i in range(len(queue)-k):
        queue.insert(0, queue.pop())
    for i in range(k):
        stack.append(queue.pop())

    while len(stack)>0:
        queue.insert(0, stack.pop())
    print(queue)

reverse([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 5)