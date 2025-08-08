import numpy as np

# to fit the second degree curve y = a*x + b*x + c*x^2 to the given data using least square method
x = np.array(list(map(float, input("Enter all x data: ").split())))
y = np.array(list(map(float, input("Enter all y data: ").split())))

n = len(x)
A = [
    [n, np.sum(x), np.sum(x**2)],
    [np.sum(x), np.sum(x**2), np.sum(x**3)],
    [np.sum(x**2), np.sum(x**3), np.sum(x**4)]
]
B = [
    [np.sum(y)],
    [np.sum(x * y)],
    [np.sum(x**2 * y)]
]

print('The coefficient matrix of the normal equations:\n', np.matrix(A))
print('The constants of the normal equations:\n', np.matrix(B))
inv_A = np.linalg.inv(A)
A = np.array(A)
B = np.array(B)
inv_A = np.linalg.inv(A)
coeff = np.dot(inv_A,B)
a = coeff[0]
b = coeff[1]
c = coeff [2]
print (f'The curve of best fit is y = {a}+{b}x+{c}x^2')


#plotting
import matplotlib.pyplot as plt
X =np.linspace(min(x)-10, max(x)+10, 1000)
plt.plot(X, a+b*X+c*X**2, color='r', label="y=a+bX+cx^2")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.scatter(x,y, color="blue", label = "data points")
plt.show()

#input
# Enter all x data: 1 2 3 4 5
# Enter all y data: 1090 1225 1390 1625 1915
# The coefficient matrix of the normal equations:
#  [[  5.  15.  55.]
#  [ 15.  55. 225.]
#  [ 55. 225. 979.]]
# The constants of the normal equations:
#  [[ 7245.]
#  [23785.]
#  [92375.]]
# The curve of best fit is y = [1024.]+[42.14285714]x+[27.14285714]x^2