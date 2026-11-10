'''
analytical_sol.py

Script collects relevant coefficients from config.py and formulates
a desired analytical function and its corresponding domain.
'''

import numpy as np

def domain(settings):
    '''
    Defines the domain for the analytical solution

    Arguments:
        settings: Dict

    Outputs:
        domain: NumPy array
    '''

    # Extract coefficients from dictionary
    x0 = settings['variables']['x0']
    xn = settings['variables']['xn']
    n = settings['variables']['n']

    # Create domain array
    domain = np.linspace(x0,xn,n+1)

    return domain

def analytical_eq(settings):
    '''
    Formulates the analytical solution array

    Arguments:
        settings: Dict

    Outputs:
        ana_sol: NumPy array
    '''
    # Define domain
    x = domain(settings)

    # User must formulate analytical equation HERE
    ana_eq = 1/2 * settings['B_coeffs']['const'] * x**2 + (10+9.81*5/2) * x

    ana_sol = {'domain': x, 'solution': ana_eq}
    return ana_sol