# to evaluate integral by simpson's 3/8 rule
# to evaluate integral by simpson's 3/8 rule
import numpy as np
import matplotlib.pyplot as plt

a = float(input("Enter the lower limit: "))
b = float(input("Enter the upper limit: "))

n = int(input("Enter the number of partitions (must be multiple of 3): "))
while n % 3 != 0:
    print("Simpson's 3/8 Rule requires n to be a multiple of 3.")
    n = int(input("Enter a valid number of partitions: "))

h = (b - a) / n

func = input("Enter the integrand function in terms of x using Python syntax: ")

def F(x, func):
    return eval(func)

def y(x):
    return F(x, func)

x = np.linspace(a, b, n + 1)

I = 0
S1 = 0
S2 = 0

for i in range(1, n):
    if i % 3 == 0:
        S2 += y(x[i])
    else:
        S1 += y(x[i])

I = (3 * h / 8) * (y(x[0]) + 3 * S1 + 2 * S2 + y(x[n]))

print(f"\nThe approximate integral is {I}")

plt.figure()
plt.plot(x, [y(i) for i in x], label=f"Integration of {func}")
x_val = np.linspace(a - 10, b + 10, 1000)
plt.plot(x_val, [y(x) for x in x_val])
y_val = [y(x) for x in x]
for i in range(0, n, 3):
    xs = x[i:i + 4]
    ys = y_val[i:i + 4]
    if len(xs) == 4:
        plt.fill_between(xs, ys, color='lightgreen', edgecolor='green', alpha=0.3)
plt.title("Evaluation of integration by Simpson's 3/8 rule.")
plt.legend()
plt.grid(True)
plt.show()

