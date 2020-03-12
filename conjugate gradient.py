"""Created on Tue Mar 10 18:43:14 2020
Conjugate Gradient method...
@author: Sagar Dam (DNAP)  """

#Algo taken from: https://en.wikipedia.org/wiki/Conjugate_gradient_method

import numpy as np
xtrue=np.matrix([[7.85971],[0.422926408],[-0.073592239],[-0.540643016],[0.010626163]])
A=np.matrix([[0.2,0.1,1,1,0],[0.1,4,-1,1,-1],[1,-1,60,0,-2],[1,1,0,8,4],[0,-1,-2,4,700]],dtype=float)
b=np.matrix([[1],[2],[3],[4],[5]],dtype=float)
x=np.matrix([[0],[0],[0],[0],[0]],dtype = float)
r=b-A*x

#Applying the conjugate gradient method:
p=r
for i in range(100):
    alpha=np.trace(((np.transpose(r))*r)/((np.transpose(p))*A*p))
    x=x+alpha*p
    r0=r
    r=r-alpha*(A*p)
    if np.all(abs(x-xtrue)<0.01):
        print("Answer: ")
        print(x)
        break
    else:
        beta=np.trace(((np.transpose(r))*r)/((np.transpose(r0))*r0))
        p=r+beta*p
print("required no of iterations: ",i)