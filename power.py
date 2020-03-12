''' TO FIND THE DOMINANT EIGENVALUE USING POWER METHOD
NAME: SAGAR DAM; DEPT: DNAP'''

import numpy as np
A=np.matrix([[2,-1,0],[-1,2,-1],[0,-1,2]])
x=np.matrix([[1],[0],[0]])
eig=np.linalg.eig(A)
n=100

#finding the dominant eigenvalue
for i in range(n):
    X=np.transpose((A**(i+1))*x)*x
    Y=np.transpose((A**(i))*x)*x
    e=np.trace(X)/np.trace(Y)
    err=100*abs(e-eig[0][0])/eig[0][0]
    if err<0.01:
        print("dominant eigenvalue: ",e)
        print("within the 0.01% accuracy range")
        break
print("required power to get the given 0.01% accuracy: ",i)
print()
print("The actual Dominant eighenvalue with numpy function")
print(eig[0][0])

#finding the eigenvector from power method
c=np.matrix((A**(i+1))*x)/e**(i+1)
c=c/(np.trace(((c[0][0])**2+(c[1][0])**2+(c[2][0])**2)))**0.5
print("The dominant eigenvector with that,(",i,") itns: ")
print(c)

#finding the corresponding eigenvector:
print()
print("If we find with numpy function, then: ")
print("the eigenvectors are given by:")
print(eig[1])