# https://nbviewer.jupyter.org/github/jmportilla/Python-for-Algorithms--Data-Structures--and-Interviews/blob/master/Algorithm%20Analysis%20and%20Big%20O/Big%20O%20Examples%20.ipynb
def printer(n=10):
    '''Print hello world! 10 times'''

    for x in range(n):
        print("Hello python!")
printer()

#  So the algorithm has O(1) space complexity and an O(n) time complexity

def create_list(m):
    new_list = []

    for num in range(m):
        new_list.append('new')

    return new_list

print(create_list(3))


# Wrost case and best case

def matcher(lst,match):
    # Return a boolen indicating item is in the list or not

    for item in lst:
        if item == match:
            return True
    return False

lst = [1,2,4,5,6,7,8,9]

print(matcher(lst,1))
print(matcher(lst,10))

# Here for the best case complexity is O(1) and wrost case complexity is O(n)