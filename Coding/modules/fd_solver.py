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

def get_domain(x0,xn,n):
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
        A[i,i-1] = settings['A_coeffs']['y_i-1/h2']/h**2 + settings['A_coeffs']['y_i-1/hx']/(h*x[i])
        A[i,i] = settings['A_coeffs']['y_i_const'] + settings['A_coeffs']['y_i/h2']/h**2
        A[i,i+1] = settings['A_coeffs']['y_i+1/h2']/h**2 + settings['A_coeffs']['y_i+1/hx']/(h*x[i])

    return A

def get_B_in(settings, x, h):
    '''
    FOR INSIDE THE SOURCE

    Creates an empty vector array for the right-
    hand-side of the finite difference matrix
    equation

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
    B_in = np.zeros(n+1)

    # Fill each element with the right hand side of the finite difference equation
    for i in range(1,n):
        B_in[i] = ( settings['B_coeffs_in']['const'] + settings['B_coeffs_in']['linear']*x[i] + settings['B_coeffs_in']['quadratic']*(x[i]**2) )*(h**2)

    # Fix initial and final values
    B_in[0] = settings['B_coeffs_in']['y0']
    B_in[-1] = settings['B_coeffs_in']['yn']

    return B_in

def get_B_out(settings, x, h):
    '''
    FOR OUTSIDE THE SOURCE

    Creates an empty vector array for the right-
    hand-side of the finite difference matrix
    equation

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
    B_out = np.zeros(n+1)

    # Fill each element with the right hand side of the finite difference equation
    for i in range(1,n):
        B_out[i] = ( settings['B_coeffs_out']['const'] + settings['B_coeffs_out']['linear']*x[i] + settings['B_coeffs_out']['quadratic']*(x[i]**2) )*(h**2)

    # Fix initial and final values
    B_out[0] = settings['B_coeffs_out']['y0']
    B_out[-1] = settings['B_coeffs_out']['yn']

    return B_out


def solve(settings, x, h):
    '''
    Uses matrix A and vector B to solve a finite difference
    matrix equation to give an array of y values defining the
    numerical solution for the original equation.

    Arguments:
        maths_settings: Dict
        A_coeffs: Dict
        B_coeffs: NumPy array

    Outputs:
        sol: Dict
    '''

    # Define A-matrix and B-vector for both inside and outside source
    A = get_A(settings, x, h)
    B = get_B_in(settings, x, h)

    # Solve the finite difference equation
    sol = np.linalg.solve(A,B)

    return sol

def form_solution(settings):
    '''
    Combines the interior and exterior numerical 
    solutions into a single array and domain

    Arguments:
        settings: Dict

    Output:
        num_dict: Dict
    '''

    n = settings['variables']['n']

    # Calculate define domains and calculate h
    h = get_h(settings)
    x_in = get_domain(settings['variables']['x0'], settings['variables']['b']-settings['variables']['e'], n)
    x_out = get_domain(settings['variables']['b'], settings['variables']['xn'] + settings['variables']['e'], n)

    # Solve interior
    interior = solve(settings, x_in, h)

    # Solve exterior
    exterior = solve(settings, x_out, h)

    # Combine arrays to form a domain and solution
    num_sol = np.concatenate((interior, exterior))
    x_tot = np.concatenate((x_in, x_out))

    # Form a dictionary
    num_dict = {'domain': x_tot, 'solution': num_sol}

    return num_dict