import pandas as pd
from pathlib import Path

# Path to raw data folder
data_path = Path("data/raw")

files = list(data_path.glob("*.csv"))

print(f"Total Files Found: {len(files)}")

for file in files:
    print("\n" + "="*60)
    print("FILE:", file.name)

    df = pd.read_csv(file)

    print("Shape:", df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())