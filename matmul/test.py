import numpy

# [[0 1] 
#  [2 3]]
A = numpy.arange(4).reshape((2, 2))
print(A)

# [[0 1] 
#  [2 3]] 
B = numpy.arange(4).reshape((2, 2))
print(B)

# [[0*0 1*1] = [[0 1] 
#  [2*2 3*3]]   [4 9]] 
print(A * B)
print(numpy.multiply(A, B))