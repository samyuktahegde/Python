from sys import maxint
def min_sums(array1, array2, k):
    n1 = len(array1)
    n2 = len(array2)
    if(k>n1*n2):
        print "k pairs do not exist"
        return
    index2 = [None]*n1
    while k > 0:
        for i1 in range(n1):
            
        
