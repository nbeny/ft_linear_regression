from scipy import misc

import matplotlib.pyplot as plt
import numpy as np
import math

#----------------------------------------------------------------------------------------#
# Function

global x1_sphere
global x2_sphere
global x3_sphere

x1_sphere = 1.5
x2_sphere = 2.5
x3_sphere = 0.5


def fonction(x1, x2, x3):
    r1 = x1 - x1_sphere
    r2 = x2 - x2_sphere
    r3 = x3 - x3_sphere
    return r1*r1 + r2*r2 + r3*r3


def partial_derivative(func, var=0, point=[]):
    args = point[:]

    def wraps(x):
        args[var] = x
        return func(*args)
    return misc.derivative(wraps, point[var], dx=1e-6)

#----------------------------------------------------------------------------------------#
# Plot Function


x1 = np.arange(0.0, 3.0, 0.1)
x2 = np.arange(0.0, 3.0, 0.1)
x3 = np.arange(0.0, 3.0, 0.1)

dim_x1 = x1.shape[0]
dim_x2 = x2.shape[0]
dim_x3 = x3.shape[0]

print(dim_x1)

z2 = np.zeros((dim_x1, dim_x2))
z3 = np.zeros((dim_x1, dim_x3))

for i in np.arange(dim_x1):
    for j in np.arange(dim_x2):
        r1 = x1[i] - x1_sphere
        r2 = x2[j] - x2_sphere
        r3 = 0.0 - x3_sphere
        z2[i, j] = r1*r1 + r2*r2 + r3*r3

h = plt.contourf(x1, x2, z2)
plt.savefig("gradient_descent_3d_python_x1_x2", bbox_inches='tight')
plt.close()

for i in np.arange(dim_x1):
    for j in np.arange(dim_x3):
        r1 = x1[i] - x1_sphere
        r2 = 0.0 - x2_sphere
        r3 = x3[j] - x3_sphere
        z3[i, j] = r1*r1 + r2*r2 + r3*r3

h = plt.contourf(x1, x3, z3)
plt.savefig("gradient_descent_3d_python_x1_x3", bbox_inches='tight')

#----------------------------------------------------------------------------------------#
# Gradient Descent

alpha = 0.1  # learning rate
nb_max_iter = 100  # Nb max d'iteration
eps = 0.0001  # stop condition

x1_0 = 0.0  # start point
x2_0 = 0.5
x3_0 = 0.0
z0 = fonction(x1_0, x2_0, x3_0)
plt.scatter(x1_0, x3_0)

cond = eps + 10.0  # start with cond greater than eps (assumption)
nb_iter = 0
tmp_z0 = z0
while cond > eps and nb_iter < nb_max_iter:
    tmp_x1_0 = x1_0 - alpha * \
        partial_derivative(fonction, 0, [x1_0, x2_0, x3_0])
    tmp_x2_0 = x2_0 - alpha * \
        partial_derivative(fonction, 1, [x1_0, x2_0, x3_0])
    tmp_x3_0 = x3_0 - alpha * \
        partial_derivative(fonction, 2, [x1_0, x2_0, x3_0])
    x1_0 = tmp_x1_0
    x2_0 = tmp_x2_0
    x3_0 = tmp_x3_0
    z0 = fonction(x1_0, x2_0, x3_0)
    nb_iter = nb_iter + 1
    cond = abs(tmp_z0 - z0)
    tmp_z0 = z0
    print(x1_0, x2_0, x3_0, cond)
    plt.scatter(x3_0, x1_0)

plt.title("Gradient Descent Python (3d test)")

plt.savefig("gradient_descent_23_python.png", bbox_inches='tight')
plt.show()
