import modules.fd_solver as fd_solver
import modules.graphing as graphing
import modules.get_data as get_data
from modules.config import settings, maths_settings, y_matrix_A_coeffs, x_vector_B_coeffs

def main():

    sol = fd_solver.solve(maths_settings, y_matrix_A_coeffs, x_vector_B_coeffs)
    graphing.plot_data(settings, maths_settings, sol)

    return

if __name__ == '__main__':
    main()