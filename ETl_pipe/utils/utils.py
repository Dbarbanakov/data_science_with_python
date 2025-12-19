# Reserved for util stuff - connectors, transformations.
import pandas as pd
from pathlib import Path

data_dir = Path.cwd() / "data"
duplicates_file = data_dir / "dropped_data/duplicates.csv"
nan_values_file = data_dir / "dropped_data/nan_values.csv"


def handle_duplicates(df):
    duplicate_df = df[df.duplicated()]
    load_to_csv(duplicate_df, duplicates_file)
    return df.drop_duplicates()


def handle_nan(df):
    nan_df = df[df.isnull().any(axis=1)]
    load_to_csv(nan_df, nan_values_file)
    return df.dropna(subset=["price", "car_model"])


def transform(df):
    df = handle_duplicates(df)
    df = handle_nan(df)
    df["price"] = df["price"].round(2)
    df["year_of_manufacture"] = pd.to_numeric(
        df["year_of_manufacture"], errors="coerce"
    )
    df.reset_index(drop=True, inplace=True)
    return df


def load_to_csv(df, csv_file):
    df.to_csv(csv_file, index=False)
