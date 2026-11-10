'''
config.py

Script containing dictionaries of all variables necessary for solvers
and plotting modules to function.

All changes should be made to this file only before running main.py

'''

# Dictionary containing desired labels for plots
graph_settings = {
    'NS_title': 'Numerical Solution',
    'AS_title': 'Analytical Solution',
    'xlabel': 't',
    'ylabel': r'y(t)'
}

# Dictionary defining key variables for finite difference
variables = {
    'n': 10,    # Number of divisions
    'x0': 0,   # Starting point
    'xn': 5     # End point
}

# Dictionary containing coefficients for LHS matrix in finite difference
y_matrix_A_coeffs = {
    'y_i-1': 1,         # Term to left of diagonal element
    'y_i_const': -2,    # Constant term in diagonal element
    'y_i_h': 0,         # Term propto h in diagonal element
    'y_i+1': 1          # Term to right of diagonal element
}

# Dictionary containing coefficients for RHS vector in finite difference
x_vector_B_coeffs = {
    'const': -9.81,     # For constant term
    'linear': 0,        # For linear term
    'quadratic':0,      # For quadratic term
    'y0': 0,            # Fixed initial value (use if applicable)
    'yn': 50             # Fixed final value (use if applicable)
}

# Dictionary containing all previous nested for convenience
settings = {
    "graph_settings": graph_settings,
    "variables": variables,
    "A_coeffs": y_matrix_A_coeffs,
    "B_coeffs": x_vector_B_coeffs
}