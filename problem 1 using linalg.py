#Name: SAGAR DAM; Dept: DNAP
#Problem: To solve the given linear equation using Gaussian elimination
#  USING LIBRARY FUNCTION.....

import numpy as np
a = np.array([[1,0.67,0.33],[0.45,1,0.55],[0.67,0.33,1]],dtype=float)
b = np.array([2,2,2],dtype=float)
x = np.linalg.solve(a, b)
print(x)