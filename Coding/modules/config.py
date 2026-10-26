import numpy as np

settings = {
    'title': '$y^{\prime\prime} = -g $',
    'xlabel': 'x',
    'ylabel': 'y'
}

maths_settings = {
    'n': 10,
    'x0': 0,
    'xn': 5
}

y_matrix_A_coeffs = {
    'y_i-1': 1,
    'y_i_const': -2,
    'y_i_h': 0,
    'y_i+1': 1
}

x_vector_B_coeffs = {
    'const': -9.81,
    'linear': 0,
    'quadratic':0,
    'y0':0
}