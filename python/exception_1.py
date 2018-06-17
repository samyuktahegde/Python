try:
    f = open('sample.txt')
    # var = bar_var
    if f.name == 'sample.txt':
        raise Exception
except FileNotFoundError as e:
    # print('Sorry. This file does not exist')
    print(e)
except Exception as e:
    # print('Sorry. Something went wrong')
    # print(e)
    print('Error!')
else:
    print(f.read())
    f.close()
finally:
    print('Executing finally...')
    