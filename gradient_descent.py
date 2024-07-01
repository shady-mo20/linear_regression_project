import numpy as np
from numpy.linalg import norm
from cost_function import fcost, drev

def gradient_descent_linear_regression(X, t_gt, step_size=0.01, precision=0.0001, max_iter=1000):
    examples, features = X.shape
    cur_weights = np.random.rand(features)         
    last_weights = cur_weights + 100 * precision

    print(f'Initial Random Cost: {fcost(X, t_gt, cur_weights)}')

    iteration = 0

    while norm(cur_weights - last_weights) > precision and iteration < max_iter:
        last_weights = cur_weights.copy()
        dcost_gradient = drev(X, t_gt, cur_weights)
        cur_weights = cur_weights - step_size * dcost_gradient
        print(f'Cost: {fcost(X, t_gt, cur_weights)}')
        iteration += 1

    print(f'Total Iterations {iteration}')
    print(f'Optimal Cost: {fcost(X, t_gt, cur_weights)}')
    return cur_weights
