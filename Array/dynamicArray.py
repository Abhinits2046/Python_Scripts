# Dynamic array implemantation
import ctypes

class DynamicArray(object):

    def __init__(self):
        self.n=0 # Count actual element(Default=0)
        self.capacity=1 # Default Capacity
        self.A = self.make_array(self.capacity)

    def __len__(self):
        # Return number of element stored in array
        return self.n

    def __getitems__(self,k):
        
        # Return element index k
        if not 0<=k <self.n:
            return IndexError("K is out of bonds!")
            # Check it k index is in bound
        
        return self.A[k] # Retrive calue from array at kth index

    def append(self,ele):
        # Add element at the end of array

        if self.n == self.capacity:
            self._resize(2*self.capacity)

        self.A[self.n] = ele
        self.n += 1

    def _resize(self,new_cap):
        # Return internal array to capacity new_cap
        
        B = self.make_array(new_cap) #New bigger array

        for k in range(self.n):
            B[k]=self.A[k]

        self.A=B
        self.capacity = new_cap

    def make_array(self,new_cap):

        return(new_cap * ctypes.py_object)()

arr = DynamicArray()

arr.append(1)
print(len(arr))
