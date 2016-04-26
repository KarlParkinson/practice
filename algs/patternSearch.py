def search(pat, text):
    i = 0
    j = 0
    n = len(pat)
    m = len(text)
    while ((i + n) < m):
        j = 0
        matching = True
        while (j < n and matching):
            if (pat[j] != text[i+j]):
                matching = False
            else:
                j += 1
        if (matching):
            print "found at index " + str(i)
        i += 1


search ("ar", "karlkarlkarl")
