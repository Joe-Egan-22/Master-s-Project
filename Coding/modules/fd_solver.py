##################################################################################
#                       FINITE DIFFERENCE SOLVER
##################################################################################

import numpy as np

def rhs(vars, x):
    return vars['x_i^0'] + vars['x_i']*x + vars['x_i^2']*x**2

def get_A(vars):
    n = vars['n']
    A = np.zeros((n+1,n+1))
    A[0,0] = 1
    A[n,n-1] = 2
    for i in range(1, n):
        A[i,i-1] = vars['y_i-1']
        A[i,i] = vars['y_i']
        A[i,i+1] = vars['y_i+1']

    return A

def get_B(vars, x):
    B = np.zeros(n+1)
    B[1:-1] = rhs(x, vars[''], linear, quadratic)
    B[0] = y0

    return B

def solve(vars):

    x0 = vars.iloc[0]['x0']
    xn = vars.iloc[0]['xn']
    n = vars.iloc[0]['n']
    y0 = vars.iloc[0]['y0']
    h = vars.loc[0]['h']
    xi = np.linspace(x0, xn, n+1)
    const = vars.iloc[0]['x_i^0']
    linear = vars.iloc[0]['x_i']
    quadratic = vars.iloc[0]['x_i^2']


    A = get_A(vars, xi)
    B = get_B(vars)

    y = np.linalg.solve(A,B)

    return y