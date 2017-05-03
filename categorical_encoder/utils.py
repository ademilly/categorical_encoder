"""Utils (ToBeRenamed) module exposes transpose matrix function
"""
from itertools import chain


def transpose(matrix, flatten=False):
    """Transpose a matrix in this particular context

    Keyword arguments:
    matrix -- square matrix
    flatten -- flatten matrix elements if needed
    """

    if flatten:
        return [
            list(chain.from_iterable([_[i] for _ in matrix]))
            for i in range(len(matrix[0]))
        ]

    else:
        return [
            [_[i] for _ in matrix]
            for i in range(len(matrix[0]))
        ]
