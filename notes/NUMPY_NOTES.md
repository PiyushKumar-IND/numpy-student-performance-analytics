# NumPy Notes - Topic by Topic

Each section matches a script in `scripts/`. Read the note, run the script, then change values and re-run.

## 0. What is NumPy and why use it?
NumPy (Numerical Python) provides the `ndarray`: a fast, fixed-type, N-dimensional array.
- 10-100x faster than Python lists for math (vectorised C code)
- Uses less memory (all elements share one dtype)
- Foundation of pandas, scikit-learn, matplotlib, TensorFlow, PyTorch

```python
import numpy as np
```

## 1. Array creation  (`01_array_creation.py`)
| Command | Meaning |
|---|---|
| `np.array([1,2,3])` | from list |
| `np.zeros((r,c))`, `np.ones(...)`, `np.full(shape, v)` | filled arrays |
| `np.eye(n)` | identity matrix |
| `np.arange(start, stop, step)` | like `range`, stop excluded |
| `np.linspace(a, b, n)` | n evenly spaced numbers, b included |
| `rng = np.random.default_rng(seed)` | modern random generator |
| `rng.random(n)`, `rng.integers(lo, hi, n)`, `rng.normal(mu, sd, n)` | random data |
| `a.copy()` | independent copy (`b = a` is NOT a copy) |

## 2. Attributes & dtypes  (`02_array_attributes.py`)
`a.shape` (rows, cols) | `a.ndim` | `a.size` | `a.dtype` | `a.itemsize` | `a.nbytes`
Convert type: `a.astype(np.float32)`. Mixed int/float lists become float automatically.

## 3. Indexing & slicing  (`03_indexing_slicing.py`)
- `a[i]`, `a[i, j]`, `a[-1]` (last)
- `a[start:stop:step]`, `a[:, 2]` (whole column), `a[:3, :2]`
- Fancy: `a[[0, 5, 9]]`
- **Slices are views**: changing a slice changes the original. Use `.copy()` to avoid it.

## 4. Reshape / stack / split  (`04_reshape_stack.py`)
`reshape(r, c)` (use `-1` for auto) | `.T` transpose | `flatten()` / `ravel()` | `np.newaxis`
`vstack`, `hstack`, `column_stack`, `concatenate(axis=)` | `split`, `array_split`

## 5. Vectorised math & broadcasting  (`05_math_broadcasting.py`)
Operators `+ - * / ** %` work element-wise. Functions: `sqrt exp log sin cos round floor ceil clip abs`.
**Broadcasting rule**: align shapes from the right; each pair of dimensions must be equal or one must be 1.
`(2,3) + (3,)` OK, `(2,3) + (2,1)` OK, `(2,3) + (2,)` ERROR.
Z-score: `(x - x.mean(axis=0)) / x.std(axis=0)`.

## 6. Statistics  (`06_statistics_aggregation.py`)
`sum mean median std var min max argmin argmax ptp percentile cumsum diff histogram corrcoef`
`axis=0` -> collapse rows (result per column) | `axis=1` -> collapse columns (result per row)
Correlation is -1..+1; near 0 = no linear relationship.

## 7. Boolean masks & filtering  (`07_boolean_filtering.py`)
```python
mask = a > 80                    # array of True/False
a[mask]                          # keep only True
(a > 50) & (b < 10)              # AND   (use & not 'and', and wrap in parentheses)
(a > 50) | (b < 10)              # OR
~mask                            # NOT
np.where(cond, x, y)             # vectorised if/else
np.where(cond)                   # indices where True
np.isin(a, [1, 2])  .any()  .all()  mask.sum()   # count of True
```

## 8. Sorting & unique  (`08_sorting_unique.py`)
`np.sort(a)` | `np.argsort(a)` (indices that would sort) | `-a` for descending
Sort table by column: `t[np.argsort(t[:, col])]`
`np.unique(a, return_counts=True)` | `np.searchsorted` | `np.partition` (fast top-k)

## 9. Missing values  (`09_missing_values.py`)
`np.nan` poisons normal math (`mean` -> nan). Use `np.isnan`, `np.nanmean/nansum/nanmax/nanstd`.
Fill: `np.where(np.isnan(a), np.nanmean(a), a)` | Drop rows: `a[~np.isnan(a).any(axis=1)]`

## 10. Linear algebra  (`10_linear_algebra.py`)
`A @ B` matrix multiply (vs `A * B` element-wise) | `np.linalg.inv, det, eig, solve, lstsq, matrix_rank`
Regression with NumPy: build `X` with a column of ones, `w = np.linalg.lstsq(X, y)[0]`, predict `X @ w`.

## 11. Random & file I/O  (`11_random_and_io.py`)
`rng.choice(n, k, replace=False)` | `rng.permutation(n)` (shuffle; train/test split)
`np.save/np.load` (.npy) | `np.savez` (.npz, many arrays) | `np.savetxt/np.genfromtxt/np.loadtxt` (CSV)
`np.genfromtxt(file, delimiter=",", skip_header=1, usecols=[...])` handles empty cells as NaN.

## 12. Mini project  (`12_mini_project_report.py`)
Combines loading, cleaning NaN, masks, grouping by city, grading, correlation, ranking.

## Common mistakes
1. `b = a` is not a copy -> use `a.copy()`.
2. `and`/`or` on arrays raises an error -> use `&`/`|` with parentheses.
3. Mixing shapes that don't broadcast -> check `.shape`.
4. NaN in data makes `mean()` return nan -> use `nanmean`.
5. Integer overflow with small dtypes (`int8` max 127).

## Dataset dictionary (`data/students.csv`, 500 rows)
| Column | Type | Description |
|---|---|---|
| student_id | int | 1-500 |
| age | int | 17-25 |
| gender | text | M / F |
| city | text | Delhi, Mumbai, Pune, Bengaluru, Kolkata |
| study_hours | float | daily study hours |
| attendance | float | % attendance |
| sleep_hours | float | contains 10 missing values (empty) |
| math, science, english | float | scores 0-100 |
| final_score | float | average of the 3 subjects |

## Practice exercises
1. Find the student with highest science score and their city.
2. Average final_score for students sleeping < 6 hours (handle NaN!).
3. Count students per age group (17-19, 20-22, 23-25).
4. Which subject has the highest correlation with study_hours?
5. Build a regression predicting `math` from `study_hours`, `attendance`, `sleep_hours`.
6. Split the data 70/30 and compute R^2 on the test set.
