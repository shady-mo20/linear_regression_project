import numpy as np 


def normal_equations_solution(X,y):
    return np.linalg.inv(X.T @ X) @ X.T @ y