# NumPy Learning Project

A complete, runnable NumPy project: 12 lessons, notes, and a 500-row CSV dataset.

## Setup
```bash
pip install -r requirements.txt
python generate_dataset.py     # optional: recreates data/students.csv (already included)
```

## Run
```bash
python main.py                                   # all lessons in order
python scripts/06_statistics_aggregation.py      # one lesson
```

## Structure
```
numpy_project/
 data/students.csv        500 students x 11 columns
 notes/NUMPY_NOTES.md     explanations + command cheat sheet + exercises
 scripts/01..12_*.py      one topic per file, heavily commented
 scripts/utils.py         CSV loader
 generate_dataset.py      builds the CSV with NumPy (seeded, reproducible)
 main.py                  runs everything
```

## Learning path
Read `notes/NUMPY_NOTES.md` -> run matching script -> edit the code -> do the exercises at the bottom of the notes.
