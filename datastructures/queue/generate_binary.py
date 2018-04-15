def generate_binary(n):
    queue = []
    queue.insert(0, '1')
    for i in range(n):
        b = queue.pop()
        print(b)
        queue.insert(0, b+'0')
        queue.insert(0, b+'1')

generate_binary(10)



