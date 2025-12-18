import glob
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime
import json


data_dir = "dealership_data"
target_file = "dealership_transformed_data.csv"
log_file = "dealership_logfile.txt"


def extract_from_json(path):
    return pd.read_json(path)


def extract_from_csv(path):
    return pd.read_csv(path)


def extract_from_xml(path):
    cols = ["car_model", "year_of_manufacture", "price", "fuel"]
    rows = []
    tree = ET.parse(path)
    for elem in tree.getroot():
        rows.append(
            {
                "car_model": elem.find("car_model").text,
                "year_of_manufacture": int(elem.find("year_of_manufacture").text),
                "price": float(elem.find("price").text),
                "fuel": elem.find("fuel").text,
            }
        )

    return pd.DataFrame(rows, columns=cols)


def get_df():
    return pd.DataFrame(columns=["car_model", "year_of_manufacture", "price", "fuel"])


def get_map():
    map = {}
    with open("./config/map.json") as f:
        for line in json.load(f):
            map = map | line
    return map


def extract_all(dir=data_dir):
    df = get_df()
    for file_pattern, func in get_map().items():
        filepaths = glob.glob(f"{dir}/{file_pattern}")
        for filepath in filepaths:
            new_df = eval(func)(filepath)
            df = pd.concat([df, new_df], ignore_index=True) if not df.empty else new_df
    return df


def transform(df):
    df = df.dropna(subset=["price", "car_model"])
    df = df.drop_duplicates()
    df["price"] = df["price"].round(2)
    df["year_of_manufacture"] = pd.to_numeric(
        df["year_of_manufacture"], errors="coerce"
    )
    df.reset_index(drop=True, inplace=True)
    return df


def load_to_csv(df, csv_file):
    df.to_csv(csv_file, index=False)


def log_event(message):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"{ts} - {message}\n")


log_event("ETL Job Started")

log_event("Extract phase Started")
df = extract_all()
log_event("Extract phase Ended")

log_event("Transform phase Started")
df = transform(df)
log_event("Transform phase Ended")

log_event("Load phase Started")
load_to_csv(df, target_file)
log_event("Load phase Ended")

log_event("ETL Job Ended")
print(df)
