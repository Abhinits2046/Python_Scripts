def sumlist(l):
    if l==[]:
        return(0)
    else:
        return(l[0]+sumlist(l[1:]))

lst = [1,5,8,9,5,7,1,3,6]
print("List elements Sum: ",sumlist(lst))