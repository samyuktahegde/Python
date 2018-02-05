def worst_fit(block_size, process_size):
    m = len(block_size)
    n = len(process_size)
    allocation = [None]*n
    for i in range(n):
        worst_index = -1
        for j in range(m):
            if block_size[j] >= process_size[i]:
                if worst_index == -1:
                    worst_index = j
                elif block_size[worst_index]<block_size[j]:
                    worst_index = j
        if worst_index != -1:
            allocation[i] = worst_index
            block_size[worst_index] -= process_size[i]
    for i in range(n):
        if allocation[i] != None:
            print allocation[i]+1,
        else:
            print "Not allocated",

blockSize = [100, 500, 200, 300, 600]
processSize = [212, 417, 112, 426]
worst_fit(blockSize, processSize)