"""Shared loader used by the dataset-based scripts."""
import os
import numpy as np

CSV = os.path.join(os.path.dirname(__file__), "..", "data", "students.csv")

def load():
    """Returns (numeric_array, text_dict, numeric_column_names)."""
    num_cols = ["student_id", "age", "study_hours", "attendance",
                "sleep_hours", "math", "science", "english", "final_score"]
    num_idx = [0, 1, 4, 5, 6, 7, 8, 9, 10]
    data = np.genfromtxt(CSV, delimiter=",", skip_header=1, usecols=num_idx)  # empty cells -> nan
    gender = np.genfromtxt(CSV, delimiter=",", skip_header=1, usecols=2, dtype=str)
    city = np.genfromtxt(CSV, delimiter=",", skip_header=1, usecols=3, dtype=str)
    return data, {"gender": gender, "city": city}, num_cols

def section(title):
    print("\n" + "=" * 60 + f"\n{title}\n" + "=" * 60)
