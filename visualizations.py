import numpy as np 
import matplotlib.pyplot as plt 

def visualize_cost_vs_iterations(costs):
    plt.plot(costs)
    plt.xlabel("Iterations")
    plt.ylabel("Cost")
    plt.title("Cost vs Iterations") 
    plt.show()

def plot_features_vs_target(X, t_gt):
    for i in range(X.shape[1]):
        plt.scatter(X[:, i], t_gt)
        plt.xlabel(f"Feature {i + 1}") 
        plt.ylabel("Target")
        plt.title(f"Feature {i + 1} vs Target")
        plt.show()
