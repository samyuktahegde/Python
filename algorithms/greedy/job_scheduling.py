def print_job_scheduling(job, n):
    sorted_job = sorted(job, key =  lambda x : x[2], reverse=True)
    slot = [False]*n
    result = [None]*n
    for i in range(n):
        for j in range(min([n, job[i][1]])-1, -1, -1):
            if slot[j]==False:
                result[j] = i  
                slot[j] = True 
                break
    for i in range(n):
        if slot[i] == True:
            print sorted_job[result[i]][0]

job = [ ('a', 2, 100), ('b', 1, 19), ('c', 2, 27),
                   ('d', 1, 25), ('e', 3, 15)]
n = len(job)
print_job_scheduling(job, n);
