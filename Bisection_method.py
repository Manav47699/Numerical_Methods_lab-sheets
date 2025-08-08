# Bisection method (cleaned up version)
import math
import numpy as np

eqn = input("Enter the equation in python syntax: ")

def F(x, eqn):
    return eval(eqn, {"x": x, "exp": np.exp})

def f(x):
    return F(x, eqn)

a = float(input("Enter the first initial guess: "))
b = float(input("Enter the second initial guess: "))
m = []

if f(a) * f(b) > 0:
    print(f"No root lies in the interval ({a}, {b})")

else:
    e = float(input("Enter the tolerable error: "))
    N = int(input("Enter the maximum number of iterations: "))
    i = 1

    while i <= N:
        c = (a + b) / 2
        m.append(c)
        fc = f(c)

        print(f"Iteration {i}: a = {a:.5f}, b = {b:.5f}, c = {c:.5f}, f(c) = {fc:.5f}")

        if f(a) * fc < 0:
            b = c
        else:
            a = c

        error = abs(b - a)
        if error < e:
            print(f"\n✅ Approximate root = {(a + b)/2:.5f} found in {i} iterations (tolerance: {e})")
            break

        i += 1

    if i > N:
        print(f"\n❌ Maximum iterations ({N}) reached. Solution may not have converged.")


# plotting block is give below:
import numpy as np
import matplotlib.pyplot as plt

# The 'm' list should already be populated from your bisection method logic.
# Ensure 'a' and 'b' are also defined from previous steps.

# Convert m to a NumPy array here, if it's still a list from the bisection loop.
# This should be the only 'm = np.array(m)' line in this block.
m = np.array(m)            #converts the variable m (a list) into a NumPy array.




x = np.linspace(0, 1, 1000)     #creates a numpy array "x" with 1000 values (0.001.......0.999). We put 1000 as our tolorable error is 0.001

plt.figure(figsize=(10, 6))
plt.plot(x, f(x), color='red', label=eqn)      #Plots the graph of the function f(x) against the values in the array x.
#label=eqn is for the legend() below
plt.axhline(0, color='black') # Simplified from (0,0)
plt.axvline(0, color='black') # Simplified from (0,0)
plt.legend()        #used to show that small box on the bottom right corner
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.title('Bisection Method')
plt.scatter(m, f(m))

for i, val in enumerate(m):                        #index ->> i
    plt.text(val, f(val) + 0.05, f'{i+1}')          #(x-axis, y-axis, which number to display)

plt.show()