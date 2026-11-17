"""TOPIC 4: Reshaping, stacking, splitting"""
import numpy as np
from utils import section

a = np.arange(12)

section("reshape / flatten / transpose")
m = a.reshape(3, 4)               # total size must match
print(m)
print("auto dim reshape(-1, 6):", a.reshape(-1, 6).shape)   # -1 = 'figure it out'
print("transpose:\n", m.T)
print("flatten:", m.flatten())    # copy;  ravel() returns a view when possible
print("add axis:", a[:, np.newaxis].shape)   # (12,) -> (12,1)

section("stacking")
x, y = np.array([1, 2, 3]), np.array([4, 5, 6])
print("vstack:\n", np.vstack([x, y]))
print("hstack:", np.hstack([x, y]))
print("column_stack:\n", np.column_stack([x, y]))
print("concatenate axis=0:", np.concatenate([x, y]))

section("splitting")
print(np.split(np.arange(9), 3))          # 3 equal parts
print(np.array_split(np.arange(10), 3))   # unequal allowed
