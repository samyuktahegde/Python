import re

fh = open('phone_book.txt')
for line in fh:
    if re.search(r"J.*Neu", line):
        print(line.rstrip())
fh.close()

