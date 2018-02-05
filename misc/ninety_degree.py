def ninety_degree(array):
    if len(array)>0:
        m = len(array)
        n = len(array[0])
        new_array = [[None]*m for i in range(n)]
        for r in range(m):
            for c in range(n):
                new_array[c][m-r-1] = array[r][c]
        return new_array

new_array = ninety_degree([[1, 2], [3, 4]])
print new_array
                    
                
            
