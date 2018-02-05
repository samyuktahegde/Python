def reverse(num, i, j):
    while(i<j):
        temp = num[i]
        num[i] = num[j]
        num[j] = temp
        i=i+1
        j=j+1

def next_palindrome(num, n):
    