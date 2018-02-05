def print_max_activities(s, f):
    n = len(f)
    print "The following activities are selected"
    i = 0
    print i,

    for j in xrange(n):
        if s[j] > f[i]:
            print j,
            i = j

# Driver program to test above function
s = [1 , 3 , 0 , 5 , 8 , 5]
f = [2 , 4 , 6 , 7 , 9 , 9]
print_max_activities(s , f)
