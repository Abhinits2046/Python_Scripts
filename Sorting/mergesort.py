def mergesort(A,B):
    (C,m,n)=([],len(A),len(B))
    (i,j)=(0,0)

    while (i+j)<(m+n):
        if i==m:
            C.append(B[j])
            j += 1
        elif j==n:
            C.append(A[i])
            i +=1
        elif A[i] <= B[j]:
            C.append(A[i])
            i +=1
        elif A[i] > B[j]:
            C.append(B[j])
            j+=1
        
    return(C)

# Driver Code

A = list(range(0,100,2))
B = list(range(1,75,2))
print("Length of list A: ", len(A))
print("Length od list B: ", len(B))
print("Length of merged list: ", len(mergesort(A,B)))
print(mergesort(A,B))