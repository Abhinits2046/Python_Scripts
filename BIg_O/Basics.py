# Big O Examples
# https://nbviewer.jupyter.org/github/jmportilla/Python-for-Algorithms--Data-Structures--and-Interviews/blob/master/Algorithm%20Analysis%20and%20Big%20O/Big%20O%20Examples%20.ipynb

# 1. Constant

print("Constant","\n")
def func_constant(values):
    print(values[0])
func_constant([1,2,3])

# 2. Linear

def func_lin(lst):
    ''' 
    Take in list and print all the values
    '''

    for val in lst:
        print(val)
print("\n","Linear","\n")
func_lin([1,2,3])

# 3. n^2 Quadratic

def fun_quad(lst):

    ''' 
    Prints Pair for evert item in the list.
    '''

    for item_1 in lst:
        for item_2 in lst:
            print(item_1,item_2)


print("\n","Quadratic","\n")
fun_quad([1,2,3,4])