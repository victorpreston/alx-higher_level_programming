#!/usr/bin/python3
"""Defining a function lazy_matrix_mul"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplication of 2 matrices.

    Args:
        m_a (list of lists of ints/floats): First matrix.
        m_b (list of lists of ints/floats): Second matrix.
    """

    return (np.matmul(m_a, m_b))
