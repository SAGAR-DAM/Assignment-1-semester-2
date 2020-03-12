'''Singular value decomposition of matrix
Name: SAGAR DAM;   DNAP'''

import numpy as np

A = np.array(([0,1,1],[0,1,0],[1,1,0],[0,1,0],[1,0,1]))

U = np.linalg.eigh(np.dot(A,A.T))[1] 

V  = np.linalg.eigh(np.dot(A.T,A))[1] 

S = np.dot(np.dot(U.T,A),V) 
print("The singular value decompostion is given by: ")
print("U = ",U)
print()
print("S = ",S)
print()
print("V = ",V)

print()
print("From numpy, the decomposition is given by: ")
B = np.linalg.svd(A)
print()
print(B)