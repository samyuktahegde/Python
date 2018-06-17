from functools import wraps

def my_logger(original_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_function.__name__), level=logging.INFO)
    @wraps(original_function)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args:{}, and kwargs:{}'.format(args,kwargs))
        return original_function(*args, **kwargs)
    return wrapper

def my_timer(original_function):
    import time
    @wraps(original_function)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in : {} sec'.format(original_function.__name__, t2))
        return result
    return wrapper

import time


@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print('Display info ran with arguments ({}, {})'.format(name, age))
# ==> display_info = my_logger(my_timer(display_info))
# display_info = my_timer(display_info)
# print(display_info.__name__)
display_info('Hank', 28)