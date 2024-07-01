# linear_regression_project

This project implements linear regression using both gradient descent and normal equations. The project includes several components to demonstrate the concepts of linear regression and its implementation in Python.

## Project Structure

- **cost_function.py**: Functions to calculate the cost and gradient for linear regression.
- **data_processing.py**: Functions to load and scale the diabetes dataset.
- **gradient_descent.py**: Implementation of the gradient descent algorithm.
- **normal_equations.py**: Implementation of the normal equations method.
- **visualizations.py**: Functions to visualize cost vs iterations and features vs target.
- **main.py**: Main script to run linear regression using different methods.
- **linear_regression_gui.py**: PyQt5-based GUI for running linear regression and visualizing results.
- Compiled `.pyc` files for performance optimization.

## How to Run

### Prerequisites

Make sure you have Python and the necessary libraries installed. You can install the required libraries using the following command:

```sh
pip install numpy matplotlib sklearn PyQt5
```

### Running the Main Script

You can run the linear regression using either gradient descent or normal equations by specifying the method. Here’s how you can do it:

```sh
python main.py --method gradient_descent
```

or

```sh
python main.py --method normal_equations
```

### Running the GUI

To run the graphical user interface for the linear regression project, use the following command:

```sh
python linear_regression_gui.py
```

## Project Components

### cost_function.py

Contains the following functions:

- `fcost(X, t_gt, weights)`: Calculates the cost for given features, target values, and weights.
- `drev(X, t_gt, weights)`: Computes the gradient of the cost function.

### data_processing.py

Provides functionality to load and scale the diabetes dataset:

- `load_diabetes_scaled()`: Loads the diabetes dataset and scales it using MinMaxScaler.

### gradient_descent.py

Implements the gradient descent algorithm:

- `gradient_descent_linear_regression(X, t_gt, step_size=0.01, precision=0.0001, max_iter=1000)`: Performs gradient descent to find the optimal weights.

### normal_equations.py

Implements the normal equations method:

- `normal_equations_solution(X, y)`: Computes the optimal weights using the normal equations.

### visualizations.py

Includes functions for visualizing data:

- `visualize_cost_vs_iterations(costs)`: Plots the cost versus iterations.
- `plot_features_vs_target(X, t_gt)`: Plots each feature against the target values.

### main.py

The main script to run the linear regression:

- Loads the dataset.
- Runs the specified method (gradient descent or normal equations).
- Visualizes the results.

### linear_regression_gui.py

Provides a graphical user interface using PyQt5:

- Allows the user to select the method, set parameters, and visualize results.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.



1. Open a text editor (like Notepad or VS Code) and create a new file.
2. Copy and paste the above content into the file.
3. Save the file as `README.md` in your project directory.
4. Add the file to your Git repository and push the changes to GitHub:
    ```sh
    git add README.md
    git commit -m "Add README.md"
    git push origin master
    ```

### Commit changes

**Commit summary**  
Add files via upload

**Optional extended description**  
Add an optional extended description…

**Commit directly to the main branch.**

**Create a new branch for this commit and start a pull request. Learn more about pull requests.**

By following these steps, you will have a detailed and comprehensive README.md file on GitHub, helping visitors to better understand and use your project. If you have any modifications or additions to include, you can edit the file accordingly. Don't forget to replace `path/to/your/screenshot.png` with the actual path to your screenshot image file.
