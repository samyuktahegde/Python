# def permutations(lst):
#     if len(lst) == 0:
#         return []
#     if len(lst) == 1:
#         return [lst]

#     l = []
#     for i in range(len(lst)):
#         m = lst[i]
#         remList = lst[:i]+lst[i+1:]
#         for p in permutations(remList):
#             l.append([m]+p)
#     return l

# data = list('123')

# for p in permutations(data):
#     print(p)

from itertools import permutations
l = list(permutations(range(1, 4)))
print (l)
    