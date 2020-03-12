#Name: SAGAR DAM; Dept: DNAP
#Problem: To solve the given linear equation using JACOBI METHOD

'''Algo reference: https://en.wikipedia.org/wiki/Jacobi_method'''

import numpy as np
xtrue=np.array([7.85971,0.422926408,-0.073592239,-0.540643016,0.010626163])
a=np.array([[0.2,0.1,1,1,0],[0.1,4,-1,1,-1],[1,-1,60,0,-2],[1,1,0,8,4],[0,-1,-2,4,700]],dtype=float)
b=np.array([1,2,3,4,5],dtype=float)

#setting x as an arbirary matrix
x=np.array([1,2,1,1,2],dtype=float)
y=np.array([0,0,0,0,0],dtype=float)
Z=0

#Doing the iteration
for i in range(100):
    #evaluating value of x(j) at ith iteration...
    for j in range(5):
        for k in range(5):
            if k!=j:
                Z=Z+a[j][k]*x[k]
        y[j]=(b[j]-Z)/a[j][j]
        Z=0
    x=y
    if np.all(abs(x-xtrue)<0.01):
        break
y=abs(x-xtrue)
#showing the Jacobi solution
print("The Jacobi solution is given by:")
print(x)
print()
print("The absolute errors in solution: from true value:")
print(y)
print()
print("Total no of required iterations: ",i)