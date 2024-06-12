import numpy as np
from dummy_package.dummy import sum_operation, matrix_dimension


def test_sum_operation():
    assert sum_operation(1, 2) == 3


def test_matrix_dimension():
    x = np.array([[1, 2], [3, 4]])
    assert matrix_dimension(x) == 2
    
def test_matrix_dimension_FAILED():
    x = np.array([[1, 2], [3, 4]])
    assert matrix_dimension(x) == 3