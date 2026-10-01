import numpy as np
from numpy.linalg import lstsq

# Step 1 & 2: Input matrix
if(input("Using Testcase? (y/n)\n")=="n"):
    m, n = map(int, input("Enter m and n (separated by a space): ").split())
    A = []
    print(f"Enter {m} rows of {n} elements each:")
    for _ in range(m):
        row = list(map(float, input().split()))
        A.append(row)
else:
    A = [[-3, 6, -1, 1, -7],
        [1, -2, 2, 3, -1],
        [2, -4, 5, 8, -4]]

# Step 3: Echelon form of augmented matrix
def gaussian_elimination(matrix):
    matrix = np.array(matrix, dtype=float)
    rows, cols = matrix.shape
    current_row = 0

    for col in range(cols - 1): 
        pivot_row = current_row
        while pivot_row < rows and matrix[pivot_row, col] == 0:
            pivot_row += 1
        if pivot_row == rows:
            continue
        if pivot_row != current_row:
            matrix[[current_row, pivot_row]] = matrix[[pivot_row, current_row]]
        matrix[current_row] /= matrix[current_row, col]

        for i in range(rows):
            if i != current_row:
                factor = matrix[i, col]
                matrix[i] -= factor * matrix[current_row]
        current_row += 1

    return matrix

rref_matrix = gaussian_elimination(A)
rref_matrix_rounded = np.round(rref_matrix, 0)
row_index = len(rref_matrix_rounded)
augmented_rref_matrix = np.column_stack((rref_matrix_rounded, np.zeros((row_index, 1), dtype=float)))

# Step 4: Basis for null space
import sympy as sp
matrix_sp = sp.Matrix(rref_matrix_rounded)
null_vectors=matrix_sp.nullspace()

# Step 5: Basis for row space
n = len(rref_matrix_rounded[0])
row_space_basis = [list(row) for row in rref_matrix_rounded[:row_index, :n]]
row_space_basis = [row for row in row_space_basis if any(val != 0 for val in row)]

# Step 6: Basis for column space
A_transposed = list(map(list, zip(*A)))
column_space_basis = []
for col_index in range(row_index):
    if 1 in rref_matrix_rounded[:row_index, col_index]:
        column_space_basis.append(list(A_transposed[col_index]))

# Step 7: Linear combinations
other_columns = []
for col_index, col_vector in enumerate(A_transposed):
    if col_vector not in column_space_basis:
        other_columns.append(list(col_vector))

column_space_basis_np = np.array(column_space_basis)
other_columns_np = np.array(other_columns)

coefficients = []
for col in other_columns_np:
    coeff, _, _, _ = lstsq(column_space_basis_np.T, col, rcond=None)
    coefficients.append(coeff)

# Print results
print("\n===================\nThe echelon form of the augmented matrix:")
print(augmented_rref_matrix)

print("\n===================\nBasis of null space:")
print(null_vectors)

print("\n===================\nBasis of Row space:")
for row_vector in row_space_basis:
    print(row_vector)

print("\n===================\nBasis of Column space:")
for col_vector in column_space_basis:
    print(col_vector)

print("\n===================\nLinear combinations:")
for i, col in enumerate(other_columns):
    terms = []
    for j, coeff in enumerate(coefficients[i]):
        term = f"{int(coeff)} * {column_space_basis[j]}"
        terms.append(term)
    print(f"{col} = " + " + ".join(terms))
print("\n")