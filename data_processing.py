import numpy as np 
from sklearn.preprocessing import MinMaxScaler

def load_diabetes_scaled():
    from sklearn.datasets import load_diabetes
    diabetes = load_diabetes()
    X,t=diabetes.data,diabetes.target
    X=MinMaxScaler().fit_transform(X)
    return X,t