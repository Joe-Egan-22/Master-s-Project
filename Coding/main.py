import modules.fd_solver as fd_solver
import modules.graphing as graphing
import modules.get_data as get_data
from modules.config import settings

def main():

    vars = get_data.read_data(settings)
    sol = fd_solver.solve(vars)
    graphing.plot_data(vars, sol)

    return

if __name__ == '__main__':
    main()