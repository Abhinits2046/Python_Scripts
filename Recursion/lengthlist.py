def listlen(l):
    if l == []:
        return(0)

    else:
        return(1+listlen(l[1:]))

lst = [1,2,3,4,5,6,7,7]

print(listlen(lst))