##################################################################################
#                       FINITE DIFFERENCE SOLVER
##################################################################################

import numpy as np

def get_h(maths_settings):
    x0 = maths_settings['x0']
    xn = maths_settings['xn']
    n = maths_settings['n']
    h = (xn - x0) / n
    return h

def get_domain(maths_settings):
    x0 = maths_settings['x0']
    xn = maths_settings['xn']
    n = maths_settings['n']

    domain = np.linspace(x0, xn, n-1)

    return domain


def get_A(n, h, A_coeffs):
    A = np.zeros((n+1,n+1))
    A[0,0] = 1
    A[n,n] = 1
    for i in range(1, n):
        A[i,i-1] = A_coeffs['y_i-1']
        A[i,i] = A_coeffs['y_i_const'] + A_coeffs['y_i_h']*h**2
        A[i,i+1] = A_coeffs['y_i+1']

    return A

def get_B(n, h, x, B_coeffs):
    B = np.zeros(n+1)
    B[1:-1] = ( B_coeffs['const'] + B_coeffs['linear']*x + B_coeffs['quadratic']*(x**2) )*(h**2)
    B[-1] = 50 # Added to suit problem, needs streamlining
    B[0] = B_coeffs['y0']

    return B

def solve(maths_settings, A_coeffs, B_coeffs):

    n = maths_settings['n']
    h = get_h(maths_settings)
    x = get_domain(maths_settings)

    A = get_A(n, h, A_coeffs)
    B = get_B(n, h, x, B_coeffs)

    y = np.linalg.solve(A,B)

    return y