"""TOPIC 2: Array attributes & data types"""
import numpy as np
from utils import section, load

data, text, cols = load()

section("Attributes")
print("shape :", data.shape)   # (rows, columns)
print("ndim  :", data.ndim)    # number of dimensions
print("size  :", data.size)    # total elements
print("dtype :", data.dtype)   # element type
print("itemsize (bytes per element):", data.itemsize)
print("nbytes:", data.nbytes)

section("Data types")
i = np.array([1, 2, 3]);       print(i.dtype)          # int64
f = np.array([1.0, 2, 3]);     print(f.dtype)          # float64 (upcast)
print(i.astype(np.float32).dtype)                      # convert with astype
print(np.array([1, 2, 3], dtype=np.int8).dtype)        # choose smaller type to save memory
print("text column dtype:", text["city"].dtype)        # <U9 = unicode string
print("first 5 cities:", text["city"][:5])
