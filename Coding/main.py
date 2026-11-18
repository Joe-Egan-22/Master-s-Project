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
    fd_sol_tw = fd_solver.solve(settings) # Numerical solution and corresponding domain
    nr_sol_tw = nr_solver.combine(settings, do_tot=False)
    fd_sol_quad = fd_solver.quad_correct(settings)
    nr_sol_soft = nr_solver.combine(settings, do_tot=False)
    ana_sols = analytical.collect_sols(settings) # Analytical solution and corresponding domain
    

    # Plot numerical and analytical solution
    if settings['selection']['FD_TW'] == True:
        graphing.plot_sols(settings, ana_sols['Thin_Wall'], fd_sol_tw, "Comparing Thin-Wall Approximation with Finite Difference")

    if settings['selection']['NR_TW'] == True:
        graphing.plot_sols(settings, ana_sols['Thin_Wall'], nr_sol_tw, "Comparing Thin-Wall Approximation with Newton Raphson")

    if settings['selection']['FD_Quad'] == True:
        graphing.plot_sols(settings, ana_sols['Quadratic'], fd_sol_quad, "Comparing Quadratic Approximation with Finite Difference")
    
    if settings['selection']['NR_Soft'] == True:
        graphing.plot_sols(settings, ana_sols['Thin_Wall'], nr_sol_soft, f"Testing Soft Boundary (width {nr_sol_soft['width']}) Against Thin Wall with NR")

    
    return None


if __name__ == '__main__':
    main()