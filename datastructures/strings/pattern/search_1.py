def search(pattern, text):
    M = len(pattern)
    N = len(text)

    for i in xrange(N-M+1):
        # print i
        # print text[i:M]
        if (pattern == text[i:i+M]):
            print "Pattern found at "+str(i)

txt = "AABAACAADAABAAABAA"
pat = "AABA"
search (pat, txt)