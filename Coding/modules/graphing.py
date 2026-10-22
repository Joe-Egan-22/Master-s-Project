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

def plot_data(vars, y):

    x0 = vars.iloc[0]['x0']
    xn = vars.iloc[0]['xn']
    n = vars.iloc[0]['n']
    xlabel = vars.iloc[0]['xlabel']
    ylabel = vars.iloc[0]['ylabel']
    title = 'Title'

    create_fig(xlabel, ylabel, title, n)
    x = np.linspace(x0, xn, n+1)
    plt.plot(x,y)
    plt.show()