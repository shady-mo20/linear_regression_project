
import numpy as np

def fcost(X, t_gt, weights):
    pred = np.dot(X, weights)
    loss = pred - t_gt  # (y(X^,W)- t^n)
    cost = np.sum(loss ** 2) / (2 * len(X))
    return cost

def drev(X, t_gt, weights):
    pred = np.dot(X, weights)
    loss = pred - t_gt
    dcost_gradient = np.dot(X.T, loss) / len(X)
    return dcost_gradient
