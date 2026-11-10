'''
config.py

Script containing dictionaries of all variables necessary for solvers
and plotting modules to function.

All changes should be made to this file only before running main.py

ALL EXCEPT THE ANALYTICAL SOLUTION WHICH MUST CURRENTLY BE EDITED IN THE analytical_sol.py FILE!

'''

import numpy as np

# Dictionary containing desired labels for plots
graph_settings = {
    'NS_title': 'Numerical Solution',
    'AS_title': 'Analytical Solution',
    'xlabel': 'x',
    'ylabel': r'f(x)'
}

# Dictionary defining key variables for finite difference
variables = {
    'n': 10,    # Number of divisions
    'x0': -5,    # Starting point
    'b': 0,     # Arbitrary source boundary value
    'xn': 5,     # End point
    'e': 1e-6   # Arbitrarily small division
}

# Dictionary containing coefficients for LHS matrix in finite difference
y_matrix_A_coeffs = {
    'y_i-1/h2': 1,   # Term propto h^-2 in left off-diagonal element
    'y_i-1/hx': -1,   # Term propto hx^-1 in left off-diagonal element

    'y_i_const': -27,  # Constant term in diagonal element
    'y_i/h2': -2,      # Term propto h^-2 in diagonal element

    'y_i+1/h2': 1,    # Term propto h^-2 in right off-diagonal element
    'y_i+1/hx': 1     # Term propto hx^-1 in right off-diagonal element
}

# Dictionary containing coefficients for RHS vector in finite difference (FOR INSIDE THE SOURCE)
B_coeffs_in = {
    'const': -25,           # For constant term
    'linear': 0,            # For linear term
    'quadratic':0,          # For quadratic term
    'y0': 0,               # Fixed initial value
    'yn': 1/np.sqrt(50)     # Fixed final value (use if applicable)
}

# Dictionary containing coefficients for RHS vector in finite difference (FOR OUTSIDE THE SOURCE)
B_coeffs_out = {
    'const': 0,                                   # For constant term
    'linear': 0,                                  # For linear term
    'quadratic':0,                                # For quadratic term
    'y0': 1/np.sqrt(50),                          # Field value at source boundary
    'yn': 1-np.exp(-np.sqrt(2)*variables['xn'])   # Fixed final value (use if applicable)
}

# Dictionary containing all previous nested for convenience
settings = {
    "graph_settings": graph_settings,
    "variables": variables,
    "A_coeffs": y_matrix_A_coeffs,
    "B_coeffs_in": B_coeffs_in,
    "B_coeffs_out": B_coeffs_out
}