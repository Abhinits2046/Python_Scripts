n = int(input("Input for factorial: "))

def factorial(n):
    if n==0:
        return 1
    
    else:
        return(n*factorial(n-1))

print(factorial(n))