def peak_util(array, low, high, n):
    mid = int(low + (high-low)/2)
    if (mid==0 or array[mid-1]<=array[mid]) and (mid==n-1 or array[mid+1]<=array[mid]):
        return mid
    elif (mid>0 and array[mid-1]>array[mid]):
        return peak_util(array, low, mid-1, n)
    else:
        return peak_util(array, mid+1, high, n)

def find_peak_util(array, n):
    return peak_util(array, 0, n-1, n)

array = [1, 3, 2, 4, 1, 0]
n = len(array)

print(find_peak_util(array, n))
        
        
