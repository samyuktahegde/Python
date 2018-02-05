def missing_integer(array, mean):
    size = len(array)+1
    total_sum = mean*size
    missing = total_sum - sum(array)
    return missing

array = [25, 65, 80]
mean = 50
print(missing_integer(array, mean))