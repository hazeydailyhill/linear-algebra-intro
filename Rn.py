#coding Rn
#Jianna Angeles and Haley Hill
#Last modified: Dec 22, 2022

#---- IMPORTANT INFO! ----
# - Since we are coding, vectors from Rn are represented by tuples.
# - Each member of the class Vector will have an attribute called vec_tuple, which contains the value of the vector.
#---- TO DO! ----
# - Change add method to expect another member of the Vector class as input, rather than a tuple.
#      (In the meantime, tuple1 is being used to test if the method works)
# - Change each method to return a member of the Vector class, rather than a tuple. 

class Vector:
    def __init__(self, vec_tuple):
        self.vec_tuple = vec_tuple

    #-- Adding Two Vectors ---
    #EXPECTS a vector in Rn
    #RETURNS a tuple that is the sum of self.vec_tuple and the given vector
    def add(self, tup1):
        result = []
        for i in range(len(self.vec_tuple)):
            a = self.vec_tuple[i] + tup1[i] 
            result.append(a)
        return result
    # --- Scalar Multiplication ---
    # EXPECTS a scalar
    # RETURNS a tuple that is the result of self.vec_tuple multiplied by the scalar
    # (uses the distributive rule)
    def scale(self, scalar):
        scaledVector = []
        for i in range(len(self.vec_tuple)):
            a = self.vec_tuple[i] * scalar
            scaledVector.append(a)
        return scaledVector

#-----------------------------------------------------------------------------------------------------
myVector = Vector([1, 2, 3]) #myVector is a member of the Vector class with vec_tuple value [1, 2, 3]
tuple1 = [4, 5, 6]           #tuple1 is a tuple with value [4, 5, 6] 
scalar1 = 3                 

myVector.add(tuple1)     # returns [5, 7, 9]
myVector.scale(scalar1)  # returns [3, 6, 9]

#---- WITHOUT THE CLASS VECTOR, IT LOOKED LIKE THIS! ---- 
#myVector = [1, 2, 3]      myVector is a tuple with value [1, 2, 3]
#tuple1 = [4, 5, 6]        tuple1 is a tuple with value [4, 5, 6]
#scalar1 = 3

#add(myVector, tuple1)    returns [5, 7, 9]
#scale(myVector, scalar1) returns [3, 6, 9]



