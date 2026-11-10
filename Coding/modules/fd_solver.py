'''
fd_solver:

Formulates and solved the matrix equation associated with the finite difference method.

Functions:

    get_h(maths_settings)
    get_domain(maths_settings)
    get_A(n, h, A_coeffs)
    get_B(n, h, x, B_coeffs)
    solve(maths_settings, A_coeffs, B_coeffs)

Output:

    y from solve(...)
'''

import numpy as np

def get_h(maths_settings):
    '''
    Extracts starting point (x0), end point (xn) and
    number of divisions from settings and calculates 
    step size (h)

    Arguments:
        maths_settings: dict

    Output:
        h: float
    '''

    # Extract coefficients from dictionary
    x0 = maths_settings['x0']
    xn = maths_settings['xn']
    n = maths_settings['n']

    # Calculate step length
    h = (xn - x0) / n
    return h

def get_domain(maths_settings):
    '''
    Extracts starting point (x0), end point (xn)
    and number of divisions (n) from settings and 
    creates an array which defines the domain of
    consideration.

    Arguments:
        maths_settings: dict

    Outputs:
        domain: NumPy array
    '''

    # Extract coefficients from dictionary
    x0 = maths_settings['x0']
    xn = maths_settings['xn']
    n = maths_settings['n']

    # Create array between x0, xn with n values
    domain = np.linspace(x0, xn, n-1)
    return domain


def get_A(n, h, A_coeffs):
    '''
    Creates an empty matrix array for the left-
    hand-side of the finite difference matrix
    equation.

    Arguments:
        n: int
        h: float
        A_coeffs: dict

    Outputs:
        A: NumPy array
    '''

    # Create empty nxn zero matrix
    A = np.zeros((n+1,n+1))

    # Set top left and bottom right values to 1
    # for initial/final value boundary conditions
    A[0,0] = 1
    A[n,n] = 1

    # Fill rest of the rows with diagonal and off-diagonal elements
    for i in range(1, n):
        A[i,i-1] = A_coeffs['y_i-1']
        A[i,i] = A_coeffs['y_i_const'] + A_coeffs['y_i_h']*h**2
        A[i,i+1] = A_coeffs['y_i+1']

    return A

def get_B(n, h, x, B_coeffs):
    '''
    Creates an empty vector array for the right-
    hand-side of the finite difference matrix
    equation.

    Arguments:
        n: int
        h: float
        x: NumPy array
        B_coeffs: Dict

    Outputs:
        B: NumPy array
    '''

    # Create empty n-length zero vector
    B = np.zeros(n+1)

    # Fill each element with the right hand side of the finite difference equation
    B[1:-1] = ( B_coeffs['const'] + B_coeffs['linear']*x + B_coeffs['quadratic']*(x**2) )*(h**2)

    # Fix initial and final values
    B[-1] = 50
    B[0] = B_coeffs['y0']

    return B

def solve(maths_settings, A_coeffs, B_coeffs):
    '''
    Uses matrix A and vector B to solve a finite difference
    matrix equation to give an array of y values defining the
    numerical solution for the original equation.

    Arguments:
        maths_settings: Dict
        A_coeffs: Dict
        B_coeffs: Dict
    '''

    # Extract required values from settings
    n = maths_settings['n']
    h = get_h(maths_settings)
    x = get_domain(maths_settings)

    # Define A-matrix and B-vector
    A = get_A(n, h, A_coeffs)
    B = get_B(n, h, x, B_coeffs)

    # Solve the finite difference equation
    y = np.linalg.solve(A,B)

    return y