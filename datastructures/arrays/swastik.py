def swastik(n):
    for i in range(n):
        for j in range(n):
            # print(i,j)
            if j==0 and i<int(n/2):
                print('*',end=' ')
            if i<int(n/2) and j>0 and j<int(n/2):
                print(' ', end=' ')
            if i==int(n/2):
                print('*',end=' ')
            if i==0 and j>n/2:
                print('*',end=' ')
            if i>int(n/2) and i<(n-1) and j>0 and j<=int(n/2):
                print(' ', end=' ')
            if i==n-1 and j>0 and j<=int(n/2):
                print('*',end=' ')
            if j==int(n/2) and i is not int(n/2):
                print('*',end=' ')
            if i>n/2 and j==n-1:
                print('*',end=' ')
            if i>n/2 and j>n/2 and j is not n-1:
                print(' ',end=' ')
                
        print()

swastik(9)
