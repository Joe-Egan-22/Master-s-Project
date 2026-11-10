'''
graphing.py

Script creates a figure and plots a solution against a domain

Functions:
    plot_data(settings, sol)
'''

import matplotlib.pyplot as plt


def plot_sols(settings, ana_sol, num_sol):
    '''
    Creates a figure and plots solution against domain.

    Arguments:
        settings: Dict
        sol: Dict

    Outputs:
        fig: Pyplot figure
    '''
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_title(settings['graph_settings']['NS_title'])
    ax.set_xlabel(settings['graph_settings']['xlabel'])
    ax.set_ylabel(settings['graph_settings']['ylabel'])

    # Plot numerical solution
    ax.plot(num_sol['domain'], num_sol['solution'], label = 'Numerical solution')
    ax.plot(ana_sol['domain'], ana_sol['solution'], label = 'Analytical solution')


    ax.legend()
    plt.show()

    return fig
    