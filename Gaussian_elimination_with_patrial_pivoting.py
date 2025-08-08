import numpy as np
import pandas as pd

n = int(input('Enter the no. of variables: '))
print('Enter augmented matrix:')
A = []
for i in range(n):
    A.append(list(map(float, input(f'Enter {i+1}th row: ').split())))

A = np.array(A)
print('The augmented matrix is:\n', A)

# Forward elimination with partial pivoting
for i in range(n):
    i_row = np.argmax(abs(A[i:, i])) + i
    A[[i, i_row]] = A[[i_row, i]]
    for j in range(i+1, n):
        A[j] = A[j] - (A[j, i] / A[i, i]) * A[i]

print('The upper triangular matrix is:')
print(np.matrix(A))

# Back-substitution
x = np.zeros(n)
for i in range(n - 1, -1, -1):
    x[i] = (A[i, n] - np.dot(A[i, i+1:n], x[i+1:n])) / A[i, i]

print('The solution is:')
for i in range(n):
    print(f'x[{i}] = {x[i]}')
