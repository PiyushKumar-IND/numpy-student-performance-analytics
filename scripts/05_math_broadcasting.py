"""TOPIC 5: Vectorised math & broadcasting
Operations apply element-by-element with no Python loops (fast!)."""
import numpy as np
from utils import section, load

section("Element-wise operations")
a = np.array([1, 2, 3]); b = np.array([10, 20, 30])
print(a + b, a * b, b / a, a ** 2, b % 7)
print("sqrt:", np.sqrt(a), "| exp:", np.exp(a).round(2), "| log:", np.log(a).round(2))
print("round/floor/ceil:", np.round(2.567, 1), np.floor(2.7), np.ceil(2.1))
print("clip:", np.clip([-5, 5, 50], 0, 10))

section("Broadcasting: smaller array is 'stretched' to match")
m = np.arange(6).reshape(2, 3)
print(m + 10)                       # scalar -> every element
print(m + np.array([100, 200, 300]))  # row vector -> every row
print(m + np.array([[1], [2]]))       # column vector -> every column
# Rule: compare shapes from the right; dims must be equal or one of them is 1.

section("Real use: normalise the dataset columns (z-score)")
data, _, cols = load()
scores = data[:, 5:8]                                 # math, science, english
z = (scores - scores.mean(axis=0)) / scores.std(axis=0)
print("z mean ~0:", z.mean(axis=0).round(6), " std ~1:", z.std(axis=0).round(6))
print("Weighted score of first 3 students:", (scores[:3] * [0.5, 0.3, 0.2]).sum(axis=1))
