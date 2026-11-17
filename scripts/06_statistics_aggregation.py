"""TOPIC 6: Aggregations & statistics.  axis=0 -> down the rows (per column)
axis=1 -> across columns (per row). NaN-safe versions start with 'nan'."""
import numpy as np
from utils import section, load

data, text, cols = load()
math = data[:, cols.index("math")]
study = data[:, cols.index("study_hours")]

section("Basic stats on math scores")
print("sum   :", math.sum())
print("mean  :", math.mean().round(2))
print("median:", np.median(math))
print("std   :", math.std().round(2), "| var:", math.var().round(2))
print("min/max:", math.min(), math.max())
print("argmin/argmax (index):", math.argmin(), math.argmax())
print("range (ptp):", np.ptp(math))
print("percentiles 25/50/75:", np.percentile(math, [25, 50, 75]))

section("axis argument")
nums = data[:, 5:8]
print("column means (math, science, english):", nums.mean(axis=0).round(2))
print("first 3 students' average:", nums.mean(axis=1)[:3].round(2))

section("Correlation: does studying help?")
print("corr(study_hours, math) =", np.corrcoef(study, math)[0, 1].round(3))
print("Correlation matrix of 4 columns:\n",
      np.corrcoef(data[:, [2, 3, 5, 8]], rowvar=False).round(2))

section("Cumulative & differences")
print(np.cumsum([1, 2, 3, 4]), np.diff([1, 4, 9, 16]))

section("Counting & histogram")
counts, edges = np.histogram(math, bins=5)
print("counts:", counts, "\nedges :", edges.round(1))
