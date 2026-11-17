"""Generates data/students.csv  (500 rows) using NumPy itself.
Run:  python generate_dataset.py
"""
import numpy as np

rng = np.random.default_rng(42)          # seed => same data every time
N = 500

student_id = np.arange(1, N + 1)
age = rng.integers(17, 26, N)
gender = rng.choice(["M", "F"], N)
city = rng.choice(["Delhi", "Mumbai", "Pune", "Bengaluru", "Kolkata"], N)
study_hours = np.clip(rng.normal(4, 1.5, N), 0.5, 10).round(1)
attendance = np.clip(rng.normal(80, 10, N), 40, 100).round(1)
sleep_hours = np.clip(rng.normal(7, 1, N), 4, 10).round(1)

def score(base_noise):
    s = 30 + study_hours * 5 + (attendance - 50) * 0.3 + rng.normal(0, base_noise, N)
    return np.clip(s, 0, 100).round(1)

math, science, english = score(8), score(8), score(8)
final = ((math + science + english) / 3).round(1)

# make ~2% of sleep_hours missing (empty cells) to practise NaN handling
sleep_str = sleep_hours.astype(str).astype(object)
sleep_str[rng.choice(N, 10, replace=False)] = ""

header = "student_id,age,gender,city,study_hours,attendance,sleep_hours,math,science,english,final_score"
with open("data/students.csv", "w") as f:
    f.write(header + "\n")
    for i in range(N):
        f.write(f"{student_id[i]},{age[i]},{gender[i]},{city[i]},{study_hours[i]},"
                f"{attendance[i]},{sleep_str[i]},{math[i]},{science[i]},{english[i]},{final[i]}\n")
print("Created data/students.csv with", N, "rows")
