#NEWTON RAPHSON METHOD
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Input equation using numpy syntax (e.g. exp(x), sin(x))
eqn = input("Enter the equation (use numpy functions like exp(x), sin(x)): ")

# Function to evaluate f(x) safely with numpy functions
def f(x):

        #'sin': np.sin,
        #'cos': np.cos,
        #'log': np.log,
       # 'sqrt': np.sqrt,
        # add more numpy functions if needed

    return eval(eqn, {
        'x': x,
        'exp': np.exp,})

# Numerical derivative (central difference)
def g(f, x, h=1e-10):
    return (f(x + h) - f(x - h)) / (2 * h)

A = []  # to store iteration data
m = []  # to store root approximations for plotting

a = float(input("Enter the initial guess: "))

if g(f, a) == 0:
    print("First derivative of the function at initial guess is zero. Try a different guess.")
else:
    e = float(input("Enter the error tolerance: "))
    N = int(input("Enter the maximum number of iterations: "))
    itr = 1
    while itr <= N:
        fa = f(a)
        ga = g(f, a)
        if ga == 0:
            print("Zero derivative encountered during iterations. Stopping.")
            break
        b = a - fa / ga
        A.append([itr, a, fa, ga, b])
        m.append(b)
        err = abs(f(b))

        if err < e:
            df = pd.DataFrame(A, columns=['Iteration', 'a', 'f(a)', "g(a)", 'b'])
            print( df.to_string(index=False))
            print(f"\nThe root of the equation is approximately: {b} in {itr} iterations")
            break
        a = b
        itr += 1
    else:
        print("Root did not converge within the given iterations.")

# Plotting
m = np.array(m)

x = np.linspace(min(m) - 5, max(m) + 5, 2000)

plt.figure(figsize=(10, 6))
plt.plot(x, f(x), label=eqn, color='purple')
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Newton-Raphson Method Root Finding')
plt.grid(True)
plt.legend()

plt.scatter(m, f(m), color='blue')

for i, val in enumerate(m):
    plt.text(val, f(val) + 0.05, f'{i+1}')

plt.show()

