def count_set_bits(n):
    count = 0
    while n:
        # count+=n&1
        # n>>=1
        n &= (n-1)
        count+=1
    return count

i = 9
print(count_set_bits(i))
