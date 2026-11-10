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

    sol from solve(...)
'''

import numpy as np

def get_h(settings):
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
    x0 = settings['variables']['x0']
    xn = settings['variables']['xn']
    n = settings['variables']['n']

    # Calculate step length
    h = (xn - x0) / n
    return h

def get_domain(settings):
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
    x0 = settings['variables']['x0']
    xn = settings['variables']['xn']
    n = settings['variables']['n']

    # Create array between x0, xn with n values
    domain = np.linspace(x0, xn, n+1)
    return domain


def get_A(settings, x, h):
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

    # Extract required coefficients
    n = settings['variables']['n']

    # Create empty nxn zero matrix
    A = np.zeros((n+1,n+1))

    # Set top left and bottom right values to 1
    # for initial/final value boundary conditions
    A[0,0] = 1
    A[n,n] = 1

    # Fill rest of the rows with diagonal and off-diagonal elements
    for i in range(1, n):
        A[i,i-1] = settings['A_coeffs']['y_i-1']
        A[i,i] = settings['A_coeffs']['y_i_const'] + settings['A_coeffs']['y_i_h']*h**2
        A[i,i+1] = settings['A_coeffs']['y_i+1']

    return A

def get_B(settings, x, h):
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

    # Extract required coefficients
    n = settings['variables']['n']

    # Create empty n-length zero vector
    B = np.zeros(n+1)

    # Fill each element with the right hand side of the finite difference equation
    for i in range(1,n):
        B[i] = ( settings['B_coeffs']['const'] + settings['B_coeffs']['linear']*x[i] + settings['B_coeffs']['quadratic']*(x[i]**2) )*(h**2)

    # Fix initial and final values
    B[0] = settings['B_coeffs']['y0']
    B[-1] = settings['B_coeffs']['yn']

    return B

def solve(settings):
    '''
    Uses matrix A and vector B to solve a finite difference
    matrix equation to give an array of y values defining the
    numerical solution for the original equation.

    Arguments:
        maths_settings: Dict
        A_coeffs: Dict
        B_coeffs: Dict

    Outputs:
        sol: Dict
    '''

    # Calculate h and define domain
    h = get_h(settings)
    x = get_domain(settings)

    # Define A-matrix and B-vector
    A = get_A(settings, x, h)
    B = get_B(settings, x, h)

    # Solve the finite difference equation
    y = np.linalg.solve(A,B)

    sol = {'domain': x, 'solution': y}
    return sol