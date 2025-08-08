#to find the dominant eigenvalue and corresponding eigenvector of a square matrix by power method

import numpy as np
import pandas as pd

def inv(a):
    try:
        return np.linalg.inv(a)
    except:
        print("The matrix is singular, cannot compute inverse!")
        exit(2)

n = int(input("Enter the order of square matrix: "))
a = []

for i in range(n):
    a.append(list(map(float, input(f"Enter the {i+1}th row: ").split())))

a = np.array(a)

print("The square matrix is:\n", np.matrix(a))

x = np.array(list(map(float, input("Enter the initial vector: ").split())))
max_ev = 0

e, N = float(input("Enter the tolerable error: ")), int(input("Enter the max no of iterations: "))
itr = 1

old_ev = 0

B = np.array(inv(a))

print(B)

table = []

while itr <= N:
    y = np.dot(B, x)
    max_ev = abs(max(y, key=abs))
    for i in range(n):
        x = y/max_ev

    err = abs(old_ev - max_ev)

    table.append({
        "Iteration": itr,
        "Eigenvalue": max_ev,
        "Eigenvector": x,
        "Error": err
    })

    if err < e:
        break
    old_ev = max_ev
    itr += 1

if itr > N:
    print(f"\nNo dominant eigenvalue found in {itr} iterations!")
else:
    print(f"\nEigenvalue found at {1/max_ev} in {itr} iterations!")
    print(f"The corresponding eigenvector is:\n", np.matrix(x))

    table = pd.DataFrame(table).to_string(index=False)
    print(table)