def grow(s):
    if len(s) == 1:
        print(s)
    else:
        grow(s[:len(s)-1])
        print(s)

grow("OHNO")
