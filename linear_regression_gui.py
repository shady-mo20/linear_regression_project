import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QComboBox, QLineEdit
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from data_processing import load_diabetes_scaled
from gradient_descent import gradient_descent_linear_regression
from normal_equations import normal_equations_solution

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class LinearRegressionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Linear Regression GUI')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.method_label = QLabel('Select Method:')
        self.method_combo = QComboBox()
        self.method_combo.addItems(['gradient_descent', 'normal_equations'])
        
        self.step_size_label = QLabel('Step Size (for Gradient Descent):')
        self.step_size_input = QLineEdit('0.01')

        self.precision_label = QLabel('Precision (for Gradient Descent):')
        self.precision_input = QLineEdit('0.0001')

        self.max_iter_label = QLabel('Max Iterations (for Gradient Descent):')
        self.max_iter_input = QLineEdit('1000')

        self.run_button = QPushButton('Run')
        self.run_button.clicked.connect(self.run_regression)

        self.result_label = QLabel('Results:')
        
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)

        layout.addWidget(self.method_label)
        layout.addWidget(self.method_combo)
        layout.addWidget(self.step_size_label)
        layout.addWidget(self.step_size_input)
        layout.addWidget(self.precision_label)
        layout.addWidget(self.precision_input)
        layout.addWidget(self.max_iter_label)
        layout.addWidget(self.max_iter_input)
        layout.addWidget(self.run_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.canvas)

        self.setLayout(layout)

    def run_regression(self):
        X, t_gt = load_diabetes_scaled()
        method = self.method_combo.currentText()
        if method == 'gradient_descent':
            step_size = float(self.step_size_input.text())
            precision = float(self.precision_input.text())
            max_iter = int(self.max_iter_input.text())
            weights = gradient_descent_linear_regression(X, t_gt, step_size, precision, max_iter)
            self.result_label.setText(f'Optimal Weights (Gradient Descent): {weights}')
        else:
            weights = normal_equations_solution(X, t_gt)
            self.result_label.setText(f'Optimal Weights (Normal Equations): {weights}')

        self.plot_cost_vs_iterations(X, t_gt, weights)

    def plot_cost_vs_iterations(self, X, t_gt, weights):
        self.canvas.axes.clear()
        pred = np.dot(X, weights)
        loss = pred - t_gt
        cost = np.sum(loss ** 2) / (2 * len(X))
        self.canvas.axes.plot(range(len(X)), loss)
        self.canvas.axes.set_xlabel("Iterations")
        self.canvas.axes.set_ylabel("Cost")
        self.canvas.axes.set_title("Cost vs Iterations")
        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LinearRegressionApp()
    ex.show()
    sys.exit(app.exec_())
