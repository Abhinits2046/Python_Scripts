def gcd(m,n):
    fm = []
    fn = []
    cf = []

    for i in range(1,m+1):
        if (m%i)==0:
            fm.append(i)

    for j in range(1,n+1):
        if (n%j)==0:
            fn.append(j)

    for f in fm:
        if f in fn:
            cf.append(f)

    return(cf[-1])
print("Greatest common devisor: ", gcd(14,63))


# Improved Gcd no use of list 
def gcd1(m1,n1):
    cf = []
    for i in range(1,min(m1,n1)+1):
        if(m1%i)==0 and (n1%i) == 0:
            cf.append(i)
    return(cf[-1])

print("improved Gcd without list :", gcd1(14,63))



# Scan backward method

def gcd2(m2,n2):
    i = min(m2,n2)

    while i>0:
        if(m2%i)==0 and (n2%i)==0:
            return(i)

        else:
            i = i-1

print("Gcd Scan backward approach: ",gcd2(14,63))
