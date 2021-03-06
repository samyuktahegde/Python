class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front == None

    def enqueue(self, data):
        temp = Node(data)
        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def dequeue(self):
        if self.is_empty():
            return
        temp = self.front
        self.front = temp.next
        if self.front == None:
            self.rear = None
        return str(temp.data)

q = Queue()
q.enqueue(10)
q.enqueue(20)
print(q.dequeue())
print(q.dequeue())
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
print(q.dequeue())