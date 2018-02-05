def prime(val):
    # import pdb; pdb.set_trace()
    for divisor in range(2, number/2):
        if number%divisor == 0:
            print "It is not a prime number"
            return 0
    print "The number is prime" 

if __name__=='__main__':
    prime(4)
