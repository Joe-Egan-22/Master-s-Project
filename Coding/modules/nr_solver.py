'''
nr_solver.py

Script to solve an ODE using a Newton-Raphson algorithm outputting the solution and its domain

Functions:


'''

import autograd as gr
import numpy as np
import matplotlib.pyplot as plt

def Fn_ext(x,y,n):
    '''
    Calculates the Fn function for Newton-Raphson
    '''

    h = (x[-1] - x[0]) / (n-1)
    ypp = (y[2:] - 2*y[1:-1] + y[:-2]) / h**2
    yp = (y[2:] - y[:-2]) / h
    return ypp + (2/x[1:-1])*yp + (1)*y[1:-1] - (y[1:-1])**3

def Fn_int(x,y,n):
    '''
    Calculates the Fn function for Newton-Raphson
    '''

    h = (x[-1] - x[0]) / (n-1)
    ypp = (y[2:] - 2*y[1:-1] + y[:-2]) / h**2
    yp = (y[2:] - y[:-2]) / h
    return ypp + (2/x[1:-1])*yp - 24*y[1:-1] - (y[1:-1])**3


def get_domain(x0, xn, n):
    '''
    Gets the domain for the problem

    Arguments:
        Settings: Dict

    Outputs:
        dom: NumPy array
    '''

    x = np.linspace(x0, xn, int(n))

    return x

def nr_solve(settings, domain, lims, J, ext):
    '''
    Solves Newton-Raphson problem, outputs solution
    and domain

    Arguments:
        Settings: Dict

    Outputs:

    '''
    # Get n
    n = settings['variables']['n']

    # Define domain
    x = domain

    # Define other
    yg = np.linspace(lims[0], lims[1], int(n/2))
    yn = yg.copy()

    # Iterative NR method
    for i in range(settings['NR_coeffs']['N_max']):
        if ext == True:
            Fy = Fn_ext(x,yg,n/2)
        else:
            Fy = Fn_int(x,yg,n/2)

        Jy = J(yg)

        delta_y = np.linalg.solve(Jy[:,1:-1], -Fy)
        yn[1:-1] = yg[1:-1] + delta_y
        if np.linalg.norm(delta_y) < settings['NR_coeffs']['tol']:
            print(f"Converged in {i+1} iterations")
            break
        else:
            yg = yn

    sol = yn

    return sol

def combine(settings):
    '''
    Combines interior and exterior solutions for Newton Raphson and returns full solution

    Arguments:

    Outputs:
    '''
    n = settings['variables']['n']
    # Define a Jacobian function

    dom_in = get_domain(settings['variables']['x0'], settings['variables']['b'], n/2)
    J_int = gr.jacobian(lambda y: Fn_int(dom_in, y, n/2))
    lim_in = (settings['B_coeffs']['y0'], settings['B_coeffs']['yb'])

    dom_out = get_domain(settings['variables']['b'], settings['variables']['xn'], n/2)
    J_ext = gr.jacobian(lambda y: Fn_ext(dom_out, y, n/2))
    lim_out = (settings['B_coeffs']['yb'], settings['B_coeffs']['yn'])


    interior = nr_solve(settings, dom_in, lim_in, J_int, ext=False)
    exterior = nr_solve(settings, dom_out, lim_out, J_ext, ext=True)

    dom = np.concatenate((dom_in, dom_out))
    sol = np.concatenate((interior, exterior))

    nr_sol = {'domain': dom, 'solution':sol}

    return nr_sol
    
'''
sol = combine(settings)

x = sol[0]
y = sol[1]

#plt.plot(x,y)
#plt.show()

print(len(x))
'''
