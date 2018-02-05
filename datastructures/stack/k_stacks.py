class k_stacks:
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.array = [None]*n
        self.top = [-1]*k
        self.next = [i+1 for i in range(n-1)]
        self.next[n-1] = -1
        self.free = 0

    def is_full():
        return (free == -1)

    def is_empty(sn):
        return (top[sn] == -1)
        
    def push(item, sn):
        if is_full():
            return
        i = free
        free = next[i]
        next[i] = top[sn]
        top[sn] = i
        array[i] = item
