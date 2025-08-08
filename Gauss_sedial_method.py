import numpy as np

n = int(input("Enter number of equations (n): "))
A = []

for i in range(n):
    row = list(map(float, input(f"Enter row {i+1} (space-separated, including constants): ").split()))
    if len(row) != n + 1:
        raise ValueError("Each row must have n coefficients + 1 constant.")
    A.append(row)

A = np.array(A)

x = []
for i in range(n):
    val = float(input(f"Enter initial guess for x{i+1}: "))
    x.append(val)

x = np.array(x)

e = float(input("Enter the tolerable error: "))
N = int(input("Enter the max number of iterations: "))

def is_diagonally_dominant(A):
    for i in range(len(A)):
        if abs(A[i][i]) < sum(abs(A[i][j]) for j in range(len(A)) if j != i):
            return False
    return True

if not is_diagonally_dominant(A[:, :-1]):
    print("Warning: The matrix is not diagonally dominant. The method may not converge.")

itr = 1
while itr <= N:
    x_old = np.copy(x)
    for i in range(n):
        sum1 = 0
        for j in range(n):
            if j != i:
                sum1 += A[i, j] * x[j]
        x[i] = (A[i, -1] - sum1) / A[i, i]

    err = np.abs(x - x_old)

    for i in range(n):
        if abs(x[i]) < 1e-10:
            x[i] = 0
        if abs(err[i]) < 1e-10:
            err[i] = 0

    print(f"Iteration {itr}: x = {np.round(x, 6)}, error = {np.round(err, 6)}")

    if np.all(err < e):
        break
    itr += 1

if itr > N:
    print(f"\nSolution did not converge in {N} iterations.")
else:
    print(f"\nSolution converged in {itr} iterations.")
    for i in range(n):
        print(f"x{i+1} = {x[i]}")
