"""TOPIC 10: Linear algebra (np.linalg) + a tiny ML example"""
import numpy as np
from utils import section, load

section("Basics")
A = np.array([[2, 1], [1, 3]]); B = np.array([[1, 0], [4, 2]])
print("A*B element-wise:\n", A * B)
print("A@B matrix product:\n", A @ B)            # same as np.dot / np.matmul
print("det:", np.linalg.det(A).round(2), "| inverse:\n", np.linalg.inv(A).round(3))
print("trace:", np.trace(A), "| rank:", np.linalg.matrix_rank(A))
vals, vecs = np.linalg.eig(A); print("eigenvalues:", vals.round(3))

section("Solve  2x + y = 5 ; x + 3y = 10")
print(np.linalg.solve(A, np.array([5, 10])))

section("Linear regression: predict final_score from study_hours & attendance")
data, _, cols = load()
X = np.column_stack([np.ones(len(data)), data[:, cols.index('study_hours')],
                     data[:, cols.index('attendance')]])        # bias column of ones
y = data[:, cols.index('final_score')]
w, *_ = np.linalg.lstsq(X, y, rcond=None)                      # least squares
print("weights [intercept, study_hours, attendance]:", w.round(3))
pred = X @ w
r2 = 1 - ((y - pred) ** 2).sum() / ((y - y.mean()) ** 2).sum()
print("R^2 =", r2.round(3), "| prediction for 6h study, 90% attendance:",
      (w @ [1, 6, 90]).round(1))
