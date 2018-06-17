# def fibonacci(n):
#     a,b,counter = 0,1,0
#     while True:
#         if(counter>n):
#             return
#         yield a
#         a,b = b, a+b
#         counter+=1

# f = fibonacci(5)
# for x in f:
#     print(x, ' ', end='')
# print()

# def fibonacci():
#     a,b = 0,1
#     while True:
#         yield a
#         a,b = b, a+b

# f = fibonacci()
# counter=0
# for x in f:
#     print(x, ' ', end='')
#     counter+=1
#     if counter>10:
#         break
# print()

# def gen():
#     yield 1
#     # raise StopIteration(42)
#     return 42

# g = gen()
# next(g)
# next(g)

# def simple_coroutine():
#     print('Coroutine has been started!')
#     x = yield
#     print('Coroutine received', x)

# cr = simple_coroutine()
# next(cr)
# cr.send('Hi')

# def infinite_looper(objects):
#     count = 0
#     while True:
#         if count>=len(objects):
#             count = 0
#         message = yield objects[count]
#         print(objects[count])
#         if message != None:
#             count = 0 if message<0 else message
#         else:
#             count+=1

# x = infinite_looper('A string with some words')
# next(x)
# x.send(9)
# x.send(10)
# x.send(100)

def infinite_looper(objects):
    count = 0
    while True:
        if count >= len(objects):
            count = 0
        try:
            message = yield objects[count]
        except Exception:
            print("index: " + str(count))
        if message != None:
            count = 0 if message < 0 else message
        else:
            count += 1

looper = infinite_looper("Python")
next(looper)
next(looper)
looper.throw(Exception)
next(looper)