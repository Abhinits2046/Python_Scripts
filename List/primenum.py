# prime number upto n
def prime(n):
    flist = []
    for i in range(1,n+1):
        if i == 2:
            flist.append(i)
        if i>1:
            for j in range(2,i+1):
                if (i%j==0):
                    break
                if j==i-1:
                    flist.append(i)
                    break
    return flist
r = int(input("Enter prime range: "))
print(prime(r))