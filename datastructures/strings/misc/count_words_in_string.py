OUT = 0
IN = 1

def count_words(string):
    state = OUT
    wc = 0

    for i in range(len(string)):
        if string[i] == ' ' or string[i] == '\n' or string[i] == '\t':
            state = OUT
        elif state == OUT:
            state = IN
            wc += 1
    return wc

# string = 'One two         three\n  four\tfive  '
string = 'One two three four five'
print('No of words:'+str(count_words(string)))
