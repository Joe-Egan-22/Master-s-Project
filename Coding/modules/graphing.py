'''
graphing.py

Script creates a figure and plots a solution against a domain

Functions:
    plot_data(settings, sol)
'''

import matplotlib.pyplot as plt

def plot_numerical_sol(settings, sol):
    '''
    Creates a figure and plots solution against domain.

    Arguments:
        settings: Dict
        sol: Dict

    Outputs:
        fig: Pyplot figure
    '''
    fig = plt.figure()
    ax = ax = fig.add_subplot()
    ax.set_title(settings['graph_settings']['NS_title'])
    ax.set_xlabel(settings['graph_settings']['xlabel'])
    ax.set_ylabel(settings['graph_settings']['ylabel'])
    #ax.legend()
    ax.plot(sol['domain'], sol['solution'])

    plt.show()

    return fig
    