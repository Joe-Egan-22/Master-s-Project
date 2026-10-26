import numpy as np
import matplotlib.pyplot as plt

def create_fig(xlabel, ylabel, title, n):

    fig, ax = plt.subplots()
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.text(0.15, 144, f'n = {n}')
    ax.legend()

    return fig

def plot_data(settings, maths_settings, sol):

    x0 = maths_settings['x0']
    xn = maths_settings['xn']
    n = maths_settings['n']
    xlabel = settings['xlabel']
    ylabel = settings['ylabel']
    title = settings['title']

    create_fig(xlabel, ylabel, title, n)
    x = np.linspace(x0, xn, n+1)
    plt.plot(x,sol)
    plt.show()