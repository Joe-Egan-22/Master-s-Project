##################################################################################
#                       FINITE DIFFERENCE SOLVER
##################################################################################

import numpy as np

def get_h(x0, xn, n):

    h = (xn - x0) / n

    return h

def rhs(h):

    return -9.81*h**2

def get_A(n, h):

    A = np.zeros((n+1,n+1))
    A[0,0] = 1
    A[n,n-1] = 2
    for i in range(1, n):
        A[i,i-1] = 1
        A[i,i] = -2 + 4*h**2
        A[i,i+1] = 1

    return A

def get_B(n, h, y0):
    B = np.zeros(n+1)
    B[1:-1] = rhs(h)
    B[0] = y0

    return B

def solve(vars):

    x0 = vars['x0']
    xn = vars['xn']
    n = vars['n']
    y0 = vars['y0']

    h = get_h(x0, xn, n)
    A = get_A(n, h)
    B = get_B(n, h, y0)

    y = np.linalg.solve(A,B)

    return y