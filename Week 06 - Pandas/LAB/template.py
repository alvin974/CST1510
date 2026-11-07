"""
RECORD CHECK - My Version

Name : Alvin Tazojr
Lane : IT
Date : 7 November 2026

Run it: python template.py
"""

import pandas as pd
from pathlib import Path

df = pd.read_csv(Path(__file__).parent / "records_sample.csv")


df["percent"] = (df["value"] / df["limit"]) * 100


print(df)