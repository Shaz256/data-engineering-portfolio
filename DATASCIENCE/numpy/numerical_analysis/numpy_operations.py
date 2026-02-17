"""
NumPy Numerical Analysis
Author: Shaziya Sayed
Purpose: Demonstrate vectorization and numerical computing
"""

import numpy as np


# =========================================================
# BASIC STATS
# =========================================================
def basic_statistics():

    sales = np.array([250, 400, 150, 600, 300, 500, 700, 200])

    print("Mean:", np.mean(sales))
    print("Median:", np.median(sales))
    print("Std Dev:", np.std(sales))
    print("Min:", np.min(sales))
    print("Max:", np.max(sales))


# =========================================================
# VECTOR OPERATIONS
# =========================================================
def vectorized_growth():

    sales = np.array([250, 400, 150, 600, 300, 500, 700, 200])

    growth = np.diff(sales)
    pct_growth = growth / sales[:-1] * 100

    print("Growth:", growth)
    print("Pct Growth:", pct_growth)


# =========================================================
# MATRIX OPERATIONS
# =========================================================
def matrix_demo():

    matrix = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    print("Transpose:\n", matrix.T)
    print("Matrix Sum:", matrix.sum())


if __name__ == "__main__":
    basic_statistics()
    vectorized_growth()
    matrix_demo()
