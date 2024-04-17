def word_cascade(s):
    grow(s)
    shrink_right(s[1:])
    
def grow(s):
    if len(s) == 1:
        print(s)
    else:
        grow(s[:len(s)-1])
        print(s)

def shrink_right(s,space=1):
    if len(s) == 0:
        print(s)
    else:
        print(" " * space + s)
        shrink_right(s[1:],space+1)

word_cascade("cascade")
