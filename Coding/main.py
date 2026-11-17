import modules.fd_solver as fd_solver
import modules.graphing as graphing
import modules.analytical_sol as analytical
import modules.variable_checker as variable_check
import modules.nr_solver as nr_solver
from modules.config import settings

def main():

    # Perform variable check
    variable_check.check_n(settings)

    # Solutions
    fd_sol = fd_solver.solve(settings) # Numerical solution and corresponding domain
    nr_sol = nr_solver.combine(settings)
    ana_sol = analytical.analytical_eq(settings) # Analytical solution and corresponding domain

    # Plot numerical and analytical solution
    if settings['selection']['FD'] == True:
        graphing.plot_sols(settings, ana_sol, fd_sol)

    if settings['selection']['NR'] == True:
        graphing.plot_sols(settings, ana_sol, nr_sol)

    return None

if __name__ == '__main__':
    main()