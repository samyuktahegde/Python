def to_string(list):
    ''.join(list)

def permute(a,l,r):
    if l==r:
        print to_string(a)
    else:
        for i in range(l, r+1):
            