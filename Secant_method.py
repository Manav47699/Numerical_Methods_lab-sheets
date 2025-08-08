import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Input the equation: use numpy functions like exp(x), sin(x), etc.
eqn = input("Enter the equation (use numpy functions like exp(x), sin(x)): ")

# Define f(x) to support both scalar and numpy array inputs using numpy functions
def f(x):

        #'sin': np.sin,
        #'cos': np.cos,
        #'log': np.log,
       # 'sqrt': np.sqrt,
        # add more numpy functions if needed

    return eval(eqn, {
        'x': x,
        'exp': np.exp,})

# Get initial guesses
a = float(input("Enter the first guess: "))
b = float(input("Enter the second guess: "))

A = []  # to store iteration info
m = []  # to store roots approximations

if f(a) == f(b):
    print("Value becomes infinite. Choose another guess.")
else:
    e = float(input("Enter the error tolerance: "))
    N = int(input("Enter the number of iterations: "))
    itr = 1
    while itr <= N:
        fa = f(a)
        fb = f(b)
        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c)
        m.append(c)
        A.append([itr, a, b, c, fa, fb, fc])
        err = abs(fc)
        if err < e:
            df = pd.DataFrame(A, columns=['itr', 'a', 'b', 'c', 'f(a)', 'f(b)', 'f(c)'])
            print(df.to_string(index=False))
            print(f"The root of the equation is: {c} in {itr} iterations")
            break
        a, b = b, c
        itr += 1
    if itr > N:
        print("Root did not converge in the given iterations")

# Plotting
m = np.array(m)

x = np.linspace(-5, +5, 2000)  # Range centered around root guesses

plt.figure(figsize=(10, 6))
plt.plot(x, f(x), label=eqn, color='red')
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Secant Method Root Finding')
plt.grid(True)
plt.legend()

plt.scatter(m, f(m), color='blue')

for i, val in enumerate(m):
    plt.text(val, f(val) + 0.05, f'{i+1}')  # slightly above each point

plt.show()
