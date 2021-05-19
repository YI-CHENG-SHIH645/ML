import numpy as np
from utils import DataLoader


def normal_equation(feature_matrix, target_values):
    A, b = feature_matrix, target_values

    # normal_eq
    weights = np.linalg.inv(A.T @ A) @ A.T @ b

    return weights


def fetch_iowa():
    cols = ['LotArea', 'OverallQual', 'OverallCond', 'SalePrice']
    data = DataLoader.load_data('iowa_original')[cols].values
    x_train, y_train = data[:2000, :3], data[:2000, -1]
    x_test, y_test = data[2000:, :3], data[2000:, -1]

    return (x_train, x_test), (y_train, y_test)
