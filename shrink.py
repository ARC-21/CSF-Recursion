def shrink(s):
    if len(s) == 1:
        print(s)
    else:
        print(s[0:len(s)])
        shrink(s[0:len(s)-1])

shrink("OHNO")
