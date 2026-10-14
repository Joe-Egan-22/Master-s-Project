
import modules.fd_solver as fd_solver
import modules.graphing as graphing
import numpy as np
vars = {
    'x0': 0,
    'xn': np.pi / 2,
    'y0': 0,
    'n': 100,
    'xlabel': 'x',
    'ylabel': 'y',
    'title': '$y^{\prime\prime} = -4y +4x $'
}

def main():

    sol = fd_solver.solve(vars)
    graphing.plot_data(vars, sol)

    return

if __name__ == '__main__':
    main()