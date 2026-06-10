import pandas as pd
import sqlite3
from pathlib import Path

db_path = "data/db/bluestock_mf.db"

conn = sqlite3.connect(db_path)

raw_path = Path("data/raw")

for file in raw_path.glob("*.csv"):

    table_name = file.stem

    df = pd.read_csv(file)

    df.to_sql(
        table_name,
        conn,
        if_exists="replace",
        index=False
    )

    print(f"Loaded: {table_name}")

conn.close()

print("Database Created Successfully!")