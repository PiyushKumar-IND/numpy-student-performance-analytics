"""Run every lesson in order:  python main.py   (or run one: python scripts/06_statistics_aggregation.py)"""
import glob, os, runpy, sys
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, "scripts"))
if not os.path.exists(os.path.join(here, "data", "students.csv")):
    runpy.run_path(os.path.join(here, "generate_dataset.py"))
for f in sorted(glob.glob(os.path.join(here, "scripts", "[0-9]*.py"))):
    print("\n" + "#" * 70 + f"\n# {os.path.basename(f)}\n" + "#" * 70)
    runpy.run_path(f)
