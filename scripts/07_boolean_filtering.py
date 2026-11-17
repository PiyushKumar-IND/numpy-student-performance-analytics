"""TOPIC 7: Boolean masks, np.where, filtering"""
import numpy as np
from utils import section, load

data, text, cols = load()
c = {n: i for i, n in enumerate(cols)}
math = data[:, c["math"]]; final = data[:, c["final_score"]]

section("Boolean mask")
mask = math > 80
print("students with math > 80:", mask.sum())
print("their ids (first 5)    :", data[mask, 0][:5])

section("Combine conditions: & (and)  | (or)  ~ (not)  -- use parentheses!")
m2 = (final >= 70) & (data[:, c["attendance"]] > 85)
print("final>=70 AND attendance>85:", m2.sum())
print("age<18 OR age>24:", ((data[:, 1] < 18) | (data[:, 1] > 24)).sum())

section("Filtering using text columns")
delhi = text["city"] == "Delhi"
print("Delhi students:", delhi.sum(), "| avg final:", final[delhi].mean().round(2))
print("Female avg final:", final[text["gender"] == "F"].mean().round(2))
for city in np.unique(text["city"]):
    print(f"  {city:10s} avg final = {final[text['city'] == city].mean():.2f}")

section("np.where: if/else for arrays")
grade = np.where(final >= 75, "A", np.where(final >= 60, "B", "C"))
print(grade[:10])
print("np.where(cond) gives indices:", np.where(math > 95)[0][:5])

section("any / all / isin")
print("anyone scored 100?", (math == 100).any(), "| all above 0?", (math > 0).all())
print("in Pune or Delhi:", np.isin(text["city"], ["Pune", "Delhi"]).sum())
