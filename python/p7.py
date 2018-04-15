# m = [[1,2], [3,4], [5,6]]
# t1 = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
# print(t1)

# matrix=[(1,2,3),(4,5,6),(7,8,9),(10,11,12)]
# t2 = zip(*matrix)
# t2list = map(list, t2)
# print(t2list) #map object

# print(map(list, zip(*matrix)))#map object
# for row in t2list:
#     print(row)

# import numpy
# matrix = [[1,2,3], [4,5,6]]
# print(numpy.transpose(matrix))

count = 0
while (count < 3):    
    count = count+1
    print("Hello Geek")

print('List Iteration')
l = ['geeks', 'for', 'geeks']
for i in l:
    print(i)

print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)

print("\nDictionary Iteration")   
d = dict() 
d['xyz'] = 123
d['abc'] = 345
for i in d :
    print("%s  %d" %(i, d[i]))