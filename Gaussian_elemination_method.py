import numpy as np

n = int(input("Enter the no of variables: "))
print("Enter augmented matrix: ")
A = []

for i in range(n):
    A.append(list(map(float, input(f"Enter row {i+1} elements: ").split())))

print("The augmented matrix is:\n", A)

A = np.array(A)

for i in range(n):
    A[i] = A[i] / A[i][i]
    for j in range(i + 1, n):
        A[j] = A[j] - A[i] * A[j][i]

print("The upper triangular matrix is:\n", A)

x = np.zeros(n)

for i in range(n - 1, -1, -1):
    x[i] = A[i][-1] - sum(A[i][j] * x[j] for j in range(i + 1, n))

print("The solution is:", x)
