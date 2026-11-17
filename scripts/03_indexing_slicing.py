"""TOPIC 3: Indexing & slicing  ->  arr[row, col]   and   arr[start:stop:step]"""
import numpy as np
from utils import section, load

data, text, cols = load()

section("Basic indexing")
print("first row         :", data[0])
print("element row0,col5 :", data[0, 5])      # math score of student 1
print("last row          :", data[-1])

section("Slicing (start:stop:step, stop excluded)")
print("first 3 rows, 3 cols:\n", data[:3, :3])
print("every 100th row, ids:", data[::100, 0])
print("column 'math'       :", data[:5, cols.index("math")])
print("reversed first 5 ids:", data[:5, 0][::-1])

section("Fancy indexing (list of positions)")
print(data[[0, 10, 20], 0])               # ids at rows 0,10,20

section("Slices are VIEWS (no copy!)")
sub = data[:2, :2]
sub[0, 0] = -1
print("original changed:", data[0, 0])
data[0, 0] = 1        # restore
