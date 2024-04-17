def snake(s, n=0):
    if n == len(s)+1:
        return
    else:
        #print(s[n-1:n])
        if n == 0:
           # print(n)
            print(s[0])
        elif n%4 == 0:
           # print(n)
            print(s[n:n+1])
        elif n%2 == 1:
            #print(n)
            print(" " + s[n:n+1])
        else:
            print("  " + s[n:n+1])
        snake(s,n+1)

snake("snakesinthegrass")



#   0
#    1
#     2
#    3
#   4
#    5
#     6
#    7
#   8
#    9
#     10
#    11
#   12
