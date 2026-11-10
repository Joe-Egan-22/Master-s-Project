import modules.fd_solver as fd_solver
import modules.graphing as graphing
from modules.config import settings

def main():

    sol = fd_solver.solve(settings)
    graphing.plot_numerical_sol(settings, sol)

    return

if __name__ == '__main__':
    main()