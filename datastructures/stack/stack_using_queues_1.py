# class Queue:
#     def __init__(self):
#         self.items = []

#     def isEmpty(self):
#         return self.items == []

#     def enqueue(self, item):
#         self.items.insert(0,item)

#     def dequeue(self):
#         return self.items.pop()

#     def size(self):
#         return len(self.items)

class Stack:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, data):
        self.q2.insert(0,data)
        if len(self.q1)>0:
            while len(self.q1)>0:
                self.q2.insert(0, self.q1.pop())
            # print(self.q1, self.q2)
        self.q1, self.q2 = self.q2, self.q1
        # print(self.q1, self.q2)

    def pop(self):
        if len(self.q1)>0:
            return self.q1.pop()
        else:
            return -1

    def print_stack(self):
        print(self.q1)

stack = Stack()
stack.push(2)
stack.push(3)
stack.push(4)
stack.print_stack()
print(stack.pop())

    

