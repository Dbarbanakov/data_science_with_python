# Reserved for util stuff - connectors, transformations.
import pandas as pd


def transform(df):
    df = df.dropna(subset=["price", "car_model"])
    df = df.drop_duplicates()
    df["price"] = df["price"].round(2)
    df["year_of_manufacture"] = pd.to_numeric(
        df["year_of_manufacture"], errors="coerce"
    )
    df.reset_index(drop=True, inplace=True)
    return df
