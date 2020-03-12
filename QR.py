''' QR DECOMPOSITION OF A GIVEN MATRIX USING NUMPY LIBRARY AND FINDING EIGENVALUES OF THE
MATRIX USING THE REPEATATING DECOMPOSITION PROCESS AND TO COMPARE THEM WITH THE ACTUAL 
EIGENVALUES GIVEN BY numpy LIBRARY FUNCTION...

NAME: SAGAR DAM ;  DEPT: DNAP'''

import numpy as np
A=np.matrix([[5,-2],[-2,8]])
c=np.linalg.eig(A)
B=np.linalg.qr(A)
print("QR decomposition of given matrix be:")
print("Q: ")
print(B[0])
print("R: ")
print(B[1])
print()

#finding eigenvalues using QR decomposition as an iterative method
for i in range(20):
    B=np.linalg.qr(A)
    A=B[1]*B[0]
print("After successive iterations the closely upper triangular matrix becomes:")
print(A)
print()
#showing the eigenvalues
for i in range(2):
    print(i+1,"th eigenvalue",A[i,i])
    
#Finding the actual eigenvalues
print()
print("Actual eigenvalues of the given matrix")
print(c[0])