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