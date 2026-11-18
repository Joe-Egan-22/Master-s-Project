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
    domain = np.linspace(x0,xn,int(n+1))

    return domain

def thin_wall_eq(settings):
    '''
    Formulates the analytical solution array of the
    thin-wall approximation

    Arguments:
        settings: Dict

    Outputs:
        ana_sol: NumPy array
    '''
    # Extract n
    n = settings['variables']['n']

    # Define domain
    x = domain(settings)
    X = settings['variables']['b'] # Arbitrary source boundary value

    # Redefine domain as difference between x and boundary source value
    s = x - np.full(n+1, X)

    # User must formulate analytical equation HERE rather than in config file

    p = 25 # Phase parameter
    g = np.sqrt(2*(p - 1)) # The effective mass of interior scalar fluctuations in units of γ
    x0 = (2 + g**2)**(-1/2) # Field boundary value
    pve_step = np.heaviside(s, 0) # Step function Theta(x) to isolate exterior
    nve_step = np.heaviside(-s, 0) # Step function Theta(-x) to isolate interior


    a = np.asinh(g/x0) - g*s
    interior = nve_step * g * (1/np.sinh(a))
    exterior = pve_step * np.tanh(s + np.atanh(x0)) # Exterior term of equation

    ana_eq = (interior + exterior)

    return ana_eq

def quadratic_eq(settings):
    '''
    Formulates the quadratic solution array of the
    thin-wall approximation

    Arguments:
        settings: Dict

    Outputs:
        ana_sol: NumPy array
    '''

    # Extract n
    n = settings['variables']['n']

    # Define domain
    x = domain(settings)
    X = settings['variables']['b'] # Arbitrary source boundary value

    # Redefine domain as difference between x and boundary source value
    s = x - np.full(n+1, X)

    # User must formulate analytical equation HERE rather than in config file

    p = 2.5 # Phase parameter
    g = np.sqrt(p-1)
    chi0 = (np.sqrt(2)*X + 1) / (X*( np.sqrt(2) + g*(np.tanh(g*X))**(-1) )) # Field boundary value
    pve_step = np.heaviside(s, 0.5) # Step function Theta(x) to isolate exterior
    nve_step = np.heaviside(-s, 0.5) # Step function Theta(-x) to isolate interior

    interior = nve_step * X/x * chi0 * np.sinh(g*x) / np.sinh(g*X)
    exterior = pve_step * (1- (1-chi0) * X/x * np.exp(np.sqrt(2)*X) * np.exp(-np.sqrt(2)*x) )

    ana_eq = (interior + exterior)

    return ana_eq

def collect_sols(settings):
    '''
    Collects all analytical solutions

    Arguments:

    Outputs:
    '''

    x = domain(settings)
    tw_sol = {'domain': x, 'solution':thin_wall_eq(settings)}
    quad_sol = {'domain': x,'solution': quadratic_eq(settings)}

    sol_dict = {
        "Thin_Wall": tw_sol,
        "Quadratic": quad_sol
    }

    return sol_dict