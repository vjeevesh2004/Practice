''' Task to be done - 
1. Create a List 
2. len
3. append
4. print
5. indexing
6. pop
7. clear
8. find
9. insert
10. delete
11. remove
'''
import ctypes #module 

class Meralist:
    def __init__(self):
        self.size = 1 # max item to be store
        self.n =  0 # num of item stored in it 
        # create a ctype array with size = self.size
        self.A = self.__make_array(self.size)
        
    def __len__(self):
        return self.n
    
    def append(self,item):
        if self.n == self.size:
            # resize
            self.__resize(self.size*2)
        
        # append
        self.A[self.n] = item
        self.n = self.n + 1
    def __resize(self, new_capacity):
        # create a new array with new capacity
        B = self.__make_array(new_capacity)
        self.size = new_capacity
    def __make_array(self,capacity):
        # creates a C array(static, referential) with size capacity            
        return (capacity*ctypes.py_object)()

L = Meralist()
print(L)
# task - 1 done, list created 

print(len(L))
# task - 2 done, length function created
