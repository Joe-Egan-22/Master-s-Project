'''
graphing.py

Script creates a figure and plots a solution against a domain

Functions:
    plot_data(settings, sol)
'''

import matplotlib.pyplot as plt
import numpy as np


def plot_sols(settings, ana_sol, num_sol, title):
    '''
    Creates a figure and plots solution against domain.

    Arguments:
        settings: Dict
        sol: Dict

    Outputs:
        fig: Pyplot figure
    '''
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title(title)
    ax.set_xlabel(settings['graph_settings']['xlabel'])
    ax.set_ylabel(settings['graph_settings']['ylabel'])

    n = settings['variables']['n']

    # Plot numerical and analytical solution
    ax.plot(num_sol['domain'], num_sol['solution'], label = f'Numerical solution (n = {n})')
    ax.plot(ana_sol['domain'], ana_sol['solution'], label = 'Analytical solution')

    # Plot vertical line indicating arbitrary source boundary position
    plt.axvline(settings['variables']['b'], color = 'r', linestyle = '--')

    ax.legend(loc = 'upper left')


    ax2 = fig.add_subplot(211)
    error = np.abs(ana_sol['solution'] - num_sol['solution']) / num_sol['solution']


    ax.set_title("% Error plot wrt numerical solution")
    ax2.plot(num_sol['domain'], error)


    plt.show()

    return fig