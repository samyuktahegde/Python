# def ref_demo(x):
#     print(x,id(x))
#     x+=42
#     print(x,id(x))
#     x=42
#     print(x,id(x))

# x = 9
# print(x,id(x))
# ref_demo(x)

def side_effects(cities):
    print(cities)
    cities+=['Birmingham', 'Bradford']
    print(cities)

locations = ['London', 'Leeds', 'Glasgow', 'Sheffield']
side_effects(locations[:])
print(locations)
