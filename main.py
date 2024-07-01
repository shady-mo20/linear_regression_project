import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from data_processing import load_diabetes_scaled
from gradient_descent import gradient_descent_linear_regression
from normal_equations import normal_equations_solution
from visualizations import visualize_cost_vs_iterations, plot_features_vs_target

def main(method, step_size=0.01, precision=0.0001, max_iter=1000):
    X, t_gt = load_diabetes_scaled()
    
    if method == 'gradient_descent':
        optimal_weights = gradient_descent_linear_regression(X, t_gt, step_size, precision, max_iter)
        print(f'Optimal Weights (Gradient Descent): {optimal_weights}')
    elif method == 'normal_equations':
        weights_ne = normal_equations_solution(X, t_gt)
        print(f'Optimal Weights (Normal Equations): {weights_ne}')
    
    plot_features_vs_target(X, t_gt)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        import argparse
        parser = argparse.ArgumentParser(description='Linear Regression using different methods')
        parser.add_argument('--method', type=str, choices=['gradient_descent', 'normal_equations'], required=True, help='Method to use for linear regression')
        parser.add_argument('--step_size', type=float, default=0.01, help='Step size for gradient descent')
        parser.add_argument('--precision', type=float, default=0.0001, help='Precision for gradient descent')
        parser.add_argument('--max_iter', type=int, default=1000, help='Maximum iterations for gradient descent')

        args = parser.parse_args()
        main(args.method, args.step_size, args.precision, args.max_iter)
    else:
       
        main('gradient_descent')
