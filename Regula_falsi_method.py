import math  # Needed for math functions like sin, exp, etc.
import numpy as np

# Input the equation
eqn = input("Enter the equation in python syntax (use 'x' as variable): ")

# Function to evaluate f(x)
def F(x, eqn):
    return eval(eqn, {"x": x, "exp": np.exp})

def f(x):
    return F(x, eqn)

# Initial guesses
a = float(input("Enter the first initial guess (a): "))
b = float(input("Enter the second initial guess (b): "))
n = []

# Check if root exists in interval
if f(a) * f(b) > 0:
    print(f"❌ No root lies in the interval ({a}, {b})")
else:
    e = float(input("Enter the tolerable error: "))
    N = int(input("Enter the maximum number of iterations: "))

    print("\n{:<10} {:<12} {:<12} {:<12} {:<12} {:<12}".format(
      "Iteration", "a", "b", "f(a)", "f(b)", "c"))
    print("-" * 70)

    i = 1
    while i <= N:
        fa = f(a)
        fb = f(b)
        c = (a * fb - b * fa) / (fb - fa)
        n.append(c)
        fc = f(c)

        print("{:<10} {:<12.5f} {:<12.5f} {:<12.5f} {:<12.5f} {:<12.5f}".format(
            i, a, b, fa, fb, c))

        if abs(fc) < e:
            print(f"\n✅ Approximate root = {c:.5f} found in {i} iterations (tolerance: {e})")
            break

        if fa * fc < 0:
            b = c
        else:
            a = c

        i += 1

    if i > N:
        print(f"\n❌ Maximum iterations ({N}) reached. Solution may not have converged.")


#plotting
import numpy as np
import matplotlib.pyplot as plt

# The 'n' list should already be populated from your Regula Falsi method logic.
# Ensure 'a' and 'b' are also defined from previous steps.

# Convert n to a NumPy array here, if it's still a list from the Regula Falsi loop.
# This should be the only 'n = np.array(n)' line in this block.

n = np.array(n)

x = np.linspace(0, 1, 1000)
plt.figure(figsize=(10, 6))
plt.plot(x, f(x), color='red', label=eqn)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.title('Regula Falsi Method')  # Changed title to Regula Falsi
if n.size > 0: # Only attempt to scatter plot if 'n' has data
    plt.scatter(n, f(n)) # Removed color and zorder for simplicity
    for i, val in enumerate(n):
        plt.text(val, f(val) + 0.05, f'{i+1}') # Fixed offset, no bbox or dynamic calculation

plt.show()