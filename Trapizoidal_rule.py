# to evaluate (∫ a to b) f(x)dx  by trapizodal rule
a = float(input("enter the lower limit: "))
b = float(input("enter the upper limit: "))
n = int(input("enter the number of partations: "))
h = (b-a)/n
function = input ("Enter the interated function in terms of x using python syntax:")
def f(x, function):
  return eval(function)
def y(x):
  return f(x, function)
x = np.linspace(a,b,n+1)
i =0       #this is ta variable to represent the intergral
s = 0       #this represents the sum of the expression inside the bracket
for i  in range (1, n):
  s += y(x[i])
i = (h/2)*(y(x[0]) + 2*s + y(x[n]))
print (f"The approprite integral value is {i}")

import numpy as np
import matplotlib.pyplot as plt

plt.plot(x, [y(xi) for xi in x], label='Data points')  # avoid overwriting x in list comprehension

x_val = np.linspace(a - 10, b + 10, 1000)
y_val = [y(xi) for xi in x_val]

plt.plot(x_val, y_val, label='Function curve')

for i in range(n):
    xs = [x[i], x[i], x[i+1], x[i+1]]
    ys = [0, y(x[i]), y(x[i+1]), 0]  # Use actual function values at x[i] and x[i+1]
    plt.fill(xs, ys, color='pink', edgecolor="blue", alpha=0.3)
plt.grid(True)
plt.title("Integration by trapezoidal rule")
plt.legend()
plt.show()

#plot
# import numpy as np
# import matplotlib.pyplot as plt

# plt.plot(x, [y(x) for x in x])
# x_val = np.linspace (a - 10, b+10, 1000)
# plt.plot(x_val, [y(x) for x in x_val])
# y_val = [y(x) for x in x_val]
# for i  in range(n):
#   xs = [x[i], x[i], x[i+1], x[i+1]]
#   ys = [0, y_val[i], y_val[i+1], 0]
#   plt.fill(xs, ys, color='pink', edgecolor = "blue", alpha = 0.3)
# plt.title("integrtion by trapizoidal rule")
# plt.plot(x_val, y_val)
# plt.show()

#input
# enter the lower limit: 0
# enter the upper limit: 6
# enter the number of partations: 6
# Enter the interated function in terms of x using python syntax:1/(1+x**2)
# The approprite integral value is 0.11578855113545704