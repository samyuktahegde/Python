# fh = open('example.txt', 'w')
# fh.write('To write or not to write\nThat is the question!\n')
# fh.close()

# with open("example.txt", "w") as fh:
#     fh.write("To write or not to write\nthat is the question!\n")

# fobj = open('ad_file.txt')
# for line in fobj:
#     print(line.rstrip())
# fobj.close()

fobj_out = open('ad_file_new.txt', 'w')
with open('ad_file.txt') as fobj:
    i = 1
    for line in fobj:
        # print(line.rstrip())
        fobj_out.write(str(i)+': '+line)
        i=i+1

fobj_out.close()

poem = open("ad_file_new.txt").readlines()
print(poem)





