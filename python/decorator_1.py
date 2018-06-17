# def outer_function(msg):
#     # message = 'Hi'
#     # message = msg
#     def inner_function():
#         # print(message)
#         print(msg)
#     return inner_function


# my_func=outer_function()
# hi_func = outer_function('Hi!')
# bye_func = outer_function('Bye!')
# hi_func()
# bye_func()

def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function

def display():
    print('display function ran')

decorated_display = decorator_function(display)
decorated_display()