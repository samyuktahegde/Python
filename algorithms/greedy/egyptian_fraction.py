def print_egyptian(nr, dr):
    if (dr==0 or nr==0):
        return
    
    if dr%nr == 0:
        print "1/%d" %(dr/nr)
        return
        
    if nr%dr == 0:
        print nr/dr
        return

    if nr>dr:
        print nr/dr
        print_egyptian(nr%dr, dr)
        return

    n = dr/nr+1
    # print n
    print "1/%d" %(n)
    # print nr*n-dr
    # print dr*n
    print_egyptian(nr*n-dr, dr*n)

nr = 6
dr = 14
print_egyptian(nr, dr)
