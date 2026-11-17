"""TOPIC 1: Creating arrays
An ndarray is NumPy's core object: a fixed-type, N-dimensional grid. It is much
faster and more memory-efficient than a Python list."""
import numpy as np
from utils import section

section("From Python lists")
a = np.array([1, 2, 3, 4])                 # 1-D
b = np.array([[1, 2, 3], [4, 5, 6]])       # 2-D (2 rows, 3 cols)
print(a, "\n", b)

section("Built-in constructors")
print("zeros   :", np.zeros((2, 3)))             # all 0.0
print("ones    :", np.ones((2, 2)))              # all 1.0
print("full    :", np.full((2, 2), 7))           # all 7
print("eye     :", np.eye(3))                    # identity matrix
print("arange  :", np.arange(0, 10, 2))          # start, stop(excl), step
print("linspace:", np.linspace(0, 1, 5))         # 5 evenly spaced points, stop INCLUDED
print("empty   :", np.empty((1, 2)).shape)       # uninitialised (fast, garbage values)

section("Random arrays (modern Generator API)")
rng = np.random.default_rng(0)
print("rand    :", rng.random(3))                # floats in [0,1)
print("integers:", rng.integers(1, 7, 5))        # like dice rolls
print("normal  :", rng.normal(0, 1, 3))          # mean 0, std 1
print("choice  :", rng.choice(["a", "b", "c"], 4))

section("Copy vs view")
x = np.array([1, 2, 3]); y = x            # same object!
y[0] = 99; print("x changed too:", x)
z = x.copy(); z[0] = 0; print("copy is independent:", x, z)
