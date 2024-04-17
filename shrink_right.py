def shrink_right(s,space=0):
    if len(s) == 0:
        print(s)
    else:
        print(" " * space + s)
        shrink_right(s[1:],space+1)

shrink_right("string")
