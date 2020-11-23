def merge(A,B):
    (C,m,n)=([],len(A),len(B))
    (i,j)=(0,0)

    while (i+j)<(m+n): #number of elements merged so far
        if i==m: # List A is empty
            C.append(B[j])
            j += 1
        elif j==n: # List B is empty
            C.append(A[i])
            i +=1
        elif A[i] <= B[j]: # Head of List A is smaller
            C.append(A[i])
            i +=1
        elif A[i] > B[j]: # Head of List B is smaller
            C.append(B[j])
            j+=1
        
    return(C)

def mergesort(A,left,right):
    if right-left <= 1: #Base case
        return(A[left:right])

    if right-left>1:
        mid = (right+left)//2

        L = mergesort(A,left,mid)
        R = mergesort(A,mid,right)

        return(merge(L,R))

# Driver Code

a = list(range(0,100,3)) + list(range(0,1000,2))

# print("Unsorted List: ",a,"\n")
print("Sorted List: ",mergesort(a,0,len(a)))
print("Length of list : ",len(a))