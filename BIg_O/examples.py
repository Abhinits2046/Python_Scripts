# check the order of given examples

# ex.1
def once(lst):
    for val in lst:
        print(val)

once([1,2,3])
print()

# The print_once() function is O(n) 

# ex.2
def print_3(lst):
    for val in lst:
        print(val)

    for val in lst:
        print(val)

    for val in lst:
        print(val)

print_3([1,2])
print()

'''We can see that the first function will print O(n) items
    and the second will print O(3n) items. However for n going to inifinity
    the constant can be dropped, since it will not have a large effect, 
    so both functions are O(n).'''
    

# ex.3 
def comp(lst):

    print(lst[0])

    midpoint = len(lst)//2

    for val in lst[:midpoint]:
        print(val)

    for x in range(10):
        print("Hello python")

lst = [1,2,3,4,5,6,7,8,9,10]
comp(lst)

''' Here after combining each operation we get order of function is (1+n/2+10)
We can see that as n grows larger the 1 and 10 terms become insignificant
and the 1/2 term multiplied against n will also not have much of an effect as n goes towards infinity.
This means the function is simply O(n)!'''