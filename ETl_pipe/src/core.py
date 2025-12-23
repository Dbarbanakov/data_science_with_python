import pandas as pd
import glob
import xml.etree.ElementTree as ET
from pathlib import Path
from utils.error_handlers import *


@error_handler
def extract_from_json(path):
    return pd.read_json(path)


@error_handler
def extract_from_csv(path):
    return pd.read_csv(path)


@error_handler
def extract_from_xml(path):
    cols = get_cols()
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


@error_handler
def extract_all(dir):
    df = pd.DataFrame(columns=get_cols())

    for file_pattern, func in get_map():
        filepaths = glob.glob(f"{dir}/{file_pattern}")
        for filepath in filepaths:
            new_df = func(filepath)
            df = pd.concat([df, new_df], ignore_index=True) if not df.empty else new_df

    return df


# Helper functions:


def get_cols():
    return ["car_model", "year_of_manufacture", "price", "fuel"]


def get_map():
    return [
        ("*.csv", extract_from_csv),
        ("*.json", extract_from_json),
        ("*.xml", extract_from_xml),
    ]
