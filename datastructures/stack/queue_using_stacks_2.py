class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, data):
            self.stack1.append(data)
        # print(self.stack1)
    
    def dequeue(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return -1
        else:
            if len(self.stack2) == 0:
                if len(self.stack1) != 0:
                    while len(self.stack1) != 0:
                        self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
                
                

    def print_queue(self):
        print(self.stack1)

queue = Queue()
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)

queue.print_queue()
print(queue.dequeue())