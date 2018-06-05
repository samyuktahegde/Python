# n = int(input('Please eter a number:'))

# while True:
#     try:
#         n = input("Please enter an integer: ")
#         n = int(n)
#         break
#     except ValueError:
#         print("No valid integer! Please try again ...")
# print("Great, you successfully entered an integer!")

# import sys

# try:
#     f = open('ad_file.txt')
#     s = f.readline()
#     i = int(s.strip())
# except IOError as e:
#     errno, strerror = e.args
#     print('I/O error ({0}): {1}'.format(errno, strerror))
# except ValueError:
#     print('No valid integer in line')
# except:
#     print('Unexpected error:', sys.exc_info()[0])
#     raise

# def f():
#     x = int("four")

# try:
#     f()
# except ValueError as e:
#     print('got it :-)', e)

# print("Let's get on")

# def f():
#     try:
#         x = int('Four')
#     except ValueError as e:
#         print('Got it in the function:-)', e)
#         raise

# try:
#     f()
# except ValueError as e:
#     print('Got it :-)', e)

# print('Let us get on')

try:
    x = float(input('Your number:'))
    inverse = 1.0/x
except ValueError as e:
    print('You should give an integer or float', e)
except ZeroDivisionError:
    print('Infinity')
else:
    print('Just printed the else block')
finally:
    print('There may or may not have been an exception')
# print('The inverse:', inverse)






