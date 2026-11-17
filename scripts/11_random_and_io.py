"""TOPIC 11: Random sampling & saving/loading files"""
import os, tempfile
import numpy as np
from utils import section, load

data, text, cols = load()
rng = np.random.default_rng(1)

section("Sampling & shuffling")
idx = rng.choice(len(data), 5, replace=False)       # 5 unique random rows
print("random student ids:", data[idx, 0].astype(int))
perm = rng.permutation(len(data))                   # shuffled indices
train, test = data[perm[:400]], data[perm[400:]]    # 80/20 split
print("train/test shapes:", train.shape, test.shape)

section("Saving & loading")
d = tempfile.mkdtemp()
np.save(os.path.join(d, "arr.npy"), data)                         # binary, exact
print("npy reload equal:", np.array_equal(np.load(os.path.join(d, "arr.npy")), data, equal_nan=True))
np.savez(os.path.join(d, "multi.npz"), a=data[:, 0], b=data[:, 1])  # several arrays
print("npz keys:", list(np.load(os.path.join(d, "multi.npz")).keys()))
np.savetxt(os.path.join(d, "top.csv"), data[:3, :4], delimiter=",", fmt="%.1f",
           header="id,age,study,attendance")                       # text CSV
print(open(os.path.join(d, "top.csv")).read())

section("Printing options")
np.set_printoptions(precision=2, suppress=True, linewidth=100)
print(data[:2])
