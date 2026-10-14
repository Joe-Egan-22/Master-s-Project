
import modules.fd_solver as fd_solver
import modules.graphing as graphing

vars = {
    'x0': 0,
    'xn': 5,
    'y0': 0,
    'yn': 50,
    'n': 10
}

def main():

    sol = fd_solver.solve(vars)

    return print(sol)

if __name__ == '__main__':
    main()