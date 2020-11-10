l = list(map(int,input("Enter the list elements using space seperator : ").split()))
def findpos(l,v):
    (found,i) = (False,0)

    while i< len(l):
        if l[i] == v:
            (found,pos) = (True,i)
            i+=1
        else:
            i+=1
    if not found:
        pos = -1
    return(pos)

print("Method1 Index : ",findpos(l,5))

# The above code will print last find index
# Below code is for first matching condition

def findpos(l,w):
    (found1, j) = (False,0)

    while j < len(l):
        if not found1 and l[j]==w:
            (found1,posn) = (True,j)
            j += 1
        else:
            j+=1
        
    if not found1:
        posn = -1

    return(posn)

print("Method 2 Index : ",findpos(l,5))