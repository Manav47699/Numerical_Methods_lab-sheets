# to solve systme of linear equations by LU decomposition method

import scipy.linalg as slg
import numpy as np

n = int(input("Enter the no. of coefficients: "))
a = []

for i in range(n):
    a.append(list(map(float, input(f"Enter the {i+1}th row: ").split())))

a = np.array(a)

print("The square matrix is:\n", np.matrix(a))

B = np.array(list(map(float, input(f"Enter the constant terms: ").split())))

print(f"The constant output matrix is:\n", B)

p, l, u = slg.lu(a)

lum = slg.lu_factor(a)

print("The lower triangular matrix is:\n", l)

print("The upper triangular matrix is:\n", u)
print("The permutation matrix is:\n", p)

x = slg.lu_solve(lum, B)

print("The solution is:\n", x)