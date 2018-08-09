# def trap_rain_water(array):
#     left = 0
#     right = len(array)-1
#     left_height = 0
#     right_height = 0
#     minimum_height = 0
#     quantity = 0
#     left_index = 0
#     right_index = 0
#     while left<=right:
#         # print('---',left, right)
#         if left_height==0:
#             if array[left]>left_height:
#                 left_height=array[left]
#                 left_index = left
#                 if right_height>0:
#                     minimum_height = min(left_height, right_height)
#             left = left+1
#         if right_height==0:
#             if array[right]>right_height:
#                 right_height=array[right]
#                 right_index = right
#                 if left_height>0:
#                     minimum_height = min(left_height, right_height)
#                 else:
#                     right = right-1
#         if minimum_height>0:
#             if array[left]>0:
#                 quantity = quantity+minimum_height*(left-left_index-1)
#                 if left<right and (minimum_height>array[left]):
#                     quantity=quantity+(minimum_height-array[left])
#                 left_index = left
#             left=left+1
#     return quantity

# print(trap_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))



def find_water(array):
    n = len(array)
    left = [0]*n
    right = [0]*n

    water = 0

    left[0] = array[0]
    for i in range(1, n):
        left[i] = max(left[i-1], array[i])     

    right[n-1] = array[n-1]
    for i in range(n-2, -1, -1):
        right[i] = max(right[i+1], array[i])

    for i in range(0,n):
        water+=min(left[i], right[i]) - array[i]

    return water          
            

print(find_water([2, 0, 2]))
            
