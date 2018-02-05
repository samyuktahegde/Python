def first_fit(block_size, process_size):
    m = len(block_size)
    n = len(process_size)
    allocation = [None]*n
    for i in range(n):
        print process_size[i],
        for j in range(m):
            if block_size[j]>=process_size[i]:
                    allocation[i] = j
                    block_size[j]-=process_size[i]
                    break
    for i in range(n):
        if allocation[i] != None:
            print allocation[i]+1,
        else:
            print "Not allocated",

blockSize = [100, 500, 200, 300, 600]
processSize = [212, 417, 112, 426]
first_fit(blockSize, processSize)