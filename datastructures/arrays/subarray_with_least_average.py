def find_min_avg_subarray(array, n, k):
    if n<k:
        return 0
    res_index = 0
    current_sum = 0
    for i in range(k):
        current_sum=current_sum+array[i]
    minimum_sum = current_sum
    for i in range(k,n):
        current_sum+=array[i]-array[i-k]
        if current_sum<minimum_sum:
            minimum_sum=current_sum
            res_index=(i-k+1)
    print(res_index, res_index+k-1)

array = [3, 7, 90, 20, 10, 50, 40]
find_min_avg_subarray(array, len(array), 3)