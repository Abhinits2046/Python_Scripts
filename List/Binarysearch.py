seq = [1,2,3,4,5,6,7,8,9,10]
l = seq[0]
r = seq[-1]
v = int(input("Enter the element to search in list: "))
def bsearch(seq,v,l,r):
    #Here l,r are the leftmost and rightmost points of the list

    if (r-l==0):
        return(False)

    mid = (r+l)//2

    if (v==mid):
        return(True)

    if(v<mid):
        return(bsearch(seq,v,l,mid))

    else:
        return(bsearch(seq,v,mid+1,r))

print(bsearch(seq,v,l,r))