def min_abs_sum_array(array):
    array.sort()
    n = len(array)
    l = 0
    r = n-1
    min_sum = array[l]+array[r]
    min_l = l
    min_r = r
    while l<r:
        sum = array[l]+array[r]
        if abs(sum)<abs(min_sum):
            min_sum = sum
            min_l = l
            min_r = r
        if sum<0:
            l+=1
        else:
            r-=1
    print(array[min_l], array[min_r], min_sum) 

array = [1, 60, -10, 70, -80, 85]
min_abs_sum_array(array);