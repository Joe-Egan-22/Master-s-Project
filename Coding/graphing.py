import numpy as np
import matplotlib.pyplot as plt

def create_fig(xlabel, ylabel):

    fig, ax = plt.subplots()
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend()

    return fig

def plot_data(x0, xlim, n, y):

    x = np.linspace(x0, xlim, n)
    plt.plot(x,y)
    plt.show()