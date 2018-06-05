import os
from contextlib import contextmanager

# cwd = os.getcwd()
# os.chdir('dir1')
# print(os.listdir())
# os.chdir(cwd)

# cwd = os.getcwd()
# os.chdir('dir2')
# print(os.listdir())
# os.chdir(cwd)

@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)

with change_dir('dir1'):
    print(os.listdir())

with change_dir('dir2'):
    print(os.listdir())

