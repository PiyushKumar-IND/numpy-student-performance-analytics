"""TOPIC 8: Sorting, ranking, unique values"""
import numpy as np
from utils import section, load

data, text, cols = load()
final = data[:, cols.index("final_score")]

section("sort vs argsort")
print("sorted (first 5):", np.sort(final)[:5])
order = np.argsort(final)[::-1]                       # indices, best first
print("Top 5 student ids :", data[order[:5], 0].astype(int))
print("Top 5 scores      :", final[order[:5]])

section("Sort whole table by a column")
by_final = data[np.argsort(-data[:, cols.index('final_score')])]   # '-' => descending
print(by_final[:3, [0, 8]])

section("unique & counts")
cities, counts = np.unique(text["city"], return_counts=True)
print({str(a): int(b) for a, b in zip(cities, counts)})
print("ages present:", np.unique(data[:, 1]).astype(int))

section("searchsorted / top-k with partition")
print("Rank position of score 70 in sorted array:", np.searchsorted(np.sort(final), 70))
print("10 largest (unordered, fast):", np.sort(np.partition(final, -10)[-10:]))
