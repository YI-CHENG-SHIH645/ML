import numpy as np


def normal_equation(feature_matrix, target_values):
    A, b = feature_matrix, target_values

    # normal_eq
    weights = np.linalg.inv(A.T @ A) @ A.T @ b

    return weights
