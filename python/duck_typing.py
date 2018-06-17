# class Duck:
#     def quack(self):
#         print('Quack, quack')

#     def fly(self):
#         print('Flap, flap!')


# class Person:
#     def quack(self):
#         print('I am quacking like a duck')

#     def fly(self):
#         print('I am flapping my arms')


# def quack_and_fly(thing):
    # if isinstance(thing, Duck):
    #     thing.quack()
    #     thing.fly()
    # else:
    #     print('This has to be a duck!')
    # thing.quack()
    # thing.fly()
    # print()

    #NonPythonic
    # if hasattr(thing, 'quack'):
    #     if callable(thing.quack):
    #         thing.quack()

    # if hasattr(thing, 'fly'):
    #     if callable(thing.fly):
    #         thing.fly()

#     try:
#         thing.quack()
#         thing.fly()
#         thing.bark()
#     except AttributeError as e:
#         print(e)

#     print()

# d = Duck()
# quack_and_fly(d)

# p = Person()
# quack_and_fly(p)

# person = {'name':'Jess', 'age':23, 'job':'Programmer'}
# person = {'name':'Jess', 'age':23}

# # #Non Pythonic
# # if 'name' in person and 'age' in person and 'job' in person:
# #     print("I'm {name}. I'm {age} years old and I am a {job}".format(**person))
# # else:
# #     print('Missing some keys')

# #EAFP
# try:
#     print("I'm {name}. I'm {age} years old and I am a {job}".format(**person))
# except KeyError as e:
#     print("Missing {} key".format(e))

# my_list = [1,2,3,4,5]

# # #Non Pythonic
# # if len(my_list)>=6:
# #     print(my_list[5])
# # else:
# #     print('That index does not exist')

# #Pythonic
# try:
#     print(my_list[5])
# except IndexError:
#     print('That index does not exist')


import os

my_file = "/tmp/test.txt"

# #Race Condition
# if os.access(my_file, os.R_OK):
#     with open(my_file) as f:
#         print(f.read())
# else:
#     print('File cannot be accessed')

#No Race Condition
try:
    f = open(my_file)
except IOError as e:
    print('File cannot be accessed')
else:
    with f:
        print(f.read())