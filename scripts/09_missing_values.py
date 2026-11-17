"""TOPIC 9: Missing data (NaN)
NaN = 'not a number'. Any normal math with NaN gives NaN, so use nan-functions."""
import numpy as np
from utils import section, load

data, _, cols = load()
sleep = data[:, cols.index("sleep_hours")]

section("Detect")
print("mean with NaN  :", sleep.mean())                 # nan !
print("NaN count      :", np.isnan(sleep).sum())
print("rows with NaN  :", np.where(np.isnan(sleep))[0])

section("Handle")
print("nanmean        :", np.nanmean(sleep).round(3))   # ignore NaN
print("nanstd/nanmax  :", np.nanstd(sleep).round(3), np.nanmax(sleep))
filled = np.where(np.isnan(sleep), np.nanmean(sleep), sleep)   # impute with mean
print("after fill NaN :", np.isnan(filled).sum(), "| mean:", filled.mean().round(3))
clean_rows = data[~np.isnan(data).any(axis=1)]           # drop any row containing NaN
print("rows before/after dropping:", data.shape[0], clean_rows.shape[0])
print("nan_to_num:", np.nan_to_num(np.array([1, np.nan, 3]), nan=0))
