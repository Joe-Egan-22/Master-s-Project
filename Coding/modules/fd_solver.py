##################################################################################
#                       FINITE DIFFERENCE SOLVER
##################################################################################

import numpy as np

def get_A(n, y_im1, y_i, y_ip1):
    A = np.zeros((n+1,n+1))
    A[0,0] = 1
    A[n,n-1] = 2
    for i in range(1, n):
        A[i,i-1] = y_im1
        A[i,i] = y_i
        A[i,i+1] = y_ip1

    return A

def get_B(n, x, const, linear, quadratic, y0):
    B = np.zeros(n+1)
    B[1:-1] = const + linear*x + quadratic*x**2
    B[0] = y0

    return B

def solve(vars):

    x0 = vars.iloc[0]['x0']
    xn = vars.iloc[0]['xn']
    n = vars.iloc[0]['n']
    y0 = vars.iloc[0]['y0']
    y_im1 = vars.iloc[0]['y_i-1']
    y_i = vars.iloc[0]['y_i']
    y_ip1 = vars.iloc[0]['y_i+1']
    h = vars.loc[0]['h']
    x = np.linspace(x0, xn, n-1)
    const = vars.iloc[0]['x_i^0']
    linear = vars.iloc[0]['x_i']
    quadratic = vars.iloc[0]['x_i^2']


    A = get_A(n, y_im1, y_i, y_ip1)
    B = get_B(n, x, const, linear, quadratic, y0)

    y = np.linalg.solve(A,B)

    return y