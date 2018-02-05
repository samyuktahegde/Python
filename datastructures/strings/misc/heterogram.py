def heterogram(input):
    alphabets = [ch for ch in input if (ord(ch) >= ord('a') and ord(ch) <= ord('z'))]
    if len(set(alphabets)) == len(alphabets):
        print "Yes"
    else:
        print "No"

input = 'the big dwarf only jumpss'
heterogram(input)
