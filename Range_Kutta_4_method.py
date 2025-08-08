# to solve insitialvalue problem of 1st order by using R-K-4 method.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
ode = input("Enter dy/dx in terms of x and y using Python syntax (e.g., x + y): ")

def F(x, y, ode):
    return eval(ode)


def f(x, y):
    return F(x, y, ode)


x = float(input("Enter the initial value of x: "))
y = float(input("Enter the initial value of y: "))
h = float(input("Enter the step size h: "))
n = int(input("Enter the number of steps: "))

# Initialize list to store results
results = [[x, y]]
x_list = [x]
y_list = [y]

# Runge-Kutta 4th-order method loop
for i in range(n):

    k1 = h * f(x, y)
    k2 = h * f(x + h/2, y + k1/2)
    k3 = h * f(x + h/2, y + k2/2)
    k4 = h * f(x + h, y + k3)

    y = y + (1/6) * (k1 + 2*k2 + 2*k3 + k4)  # FIXED parentheses issue here
    x = x + h
    results.append([x, y])
    x_list.append(x)
    y_list.append(y)

# Convert to DataFrame
df = pd.DataFrame(results, columns=['x', 'y'])

# Display results
print("\nSolution using RK4 method:")
print(df)

#plotting
plt.plot(x_list, y_list, label = ode, color = "red")
plt.legend()
plt.grid(True)
plt.show()
