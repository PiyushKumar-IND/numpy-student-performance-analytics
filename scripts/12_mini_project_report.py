"""TOPIC 12: MINI PROJECT - Student performance report using everything learned."""
import numpy as np
from utils import section, load

data, text, cols = load()
c = {n: i for i, n in enumerate(cols)}
sleep = data[:, c["sleep_hours"]]
data[:, c["sleep_hours"]] = np.where(np.isnan(sleep), np.nanmean(sleep), sleep)  # clean
final = data[:, c["final_score"]]

section("1. Overview")
print(f"Students: {len(data)} | Avg final: {final.mean():.2f} | Median: {np.median(final):.2f}")
print(f"Best: id {int(data[final.argmax(), 0])} ({final.max()}) | Worst: id {int(data[final.argmin(), 0])} ({final.min()})")

section("2. Subject averages")
for s in ["math", "science", "english"]:
    print(f"{s:8s} mean={data[:, c[s]].mean():6.2f}  std={data[:, c[s]].std():5.2f}")

section("3. City ranking")
cities = np.unique(text["city"])
avgs = np.array([final[text["city"] == ct].mean() for ct in cities])
for i in np.argsort(-avgs):
    print(f"{cities[i]:10s} {avgs[i]:.2f}")

section("4. Grades distribution")
grade = np.where(final >= 75, "A", np.where(final >= 60, "B", "C"))
g, n = np.unique(grade, return_counts=True)
print({str(a): int(b) for a, b in zip(g, n)})

section("5. Insights")
study = data[:, c["study_hours"]]
hi, lo = final[study >= 5].mean(), final[study < 3].mean()
print(f"Students studying >=5h average {hi:.1f} vs <3h average {lo:.1f}")
print("Correlation study_hours vs final:", np.corrcoef(study, final)[0, 1].round(3))
print("Correlation attendance vs final :", np.corrcoef(data[:, c['attendance']], final)[0, 1].round(3))
at_risk = (final < 50) | (data[:, c["attendance"]] < 60)
print("At-risk student ids:", data[at_risk, 0].astype(int)[:15], f"... total {at_risk.sum()}")

section("6. Top 10 students")
top = np.argsort(-final)[:10]
for r, i in enumerate(top, 1):
    print(f"{r:2d}. id {int(data[i,0]):3d}  {text['city'][i]:10s} final={final[i]}")
