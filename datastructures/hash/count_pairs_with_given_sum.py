# def get_pairs(array, sum):
#     n = len(array)
#     count=0
#     for i in range(0,n):
#         for j in range(i+1, n):
#             if (array[i]+array[j])==sum:
#                 count+=1
#     return count

def get_pairs(array, sum):
    m = [0]*1000
    n = len(array)
    for i in range(0,n):
        m[array[i]]+=1
    twice_count = 0
    for i in range(0,n):
        twice_count += m[sum-array[i]]
        if (sum-array[i])==array[i]:
            twice_count-=1

    return int(twice_count/2)
    

array = [1,5,7,-1,5]
print(get_pairs(array, 6))
