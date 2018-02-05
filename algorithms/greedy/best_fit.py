def best_fit(block_size, process_size):
    m = len(block_size)
    n = len(process_size)
    allocation = [None]*n
    for i in range(n):
        best_index = -1
        for j in range(m):
            if block_size[j] >= process_size[i]:
                if best_index == -1:
                    best_index = j
                elif block_size[best_index]>block_size[j]:
                    best_index = j
        if best_index != -1:
            allocation[i] = best_index
            block_size[best_index] -= process_size[i]
    for i in range(n):
        if allocation[i] != None:
            print allocation[i]+1,
        else:
            print "Not allocated",

blockSize = [100, 500, 200, 300, 600]
processSize = [212, 417, 112, 426]
best_fit(blockSize, processSize)