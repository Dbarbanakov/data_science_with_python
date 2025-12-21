import glob
import pandas as pd
import xml.etree.ElementTree as ET
import json
from pathlib import Path

data_dir = Path.cwd() / "data"


def error_handler(fn):
    def wrapper(path):
        try:
            return fn(path)
        except ValueError as value_error:
            return value_error
        except FileNotFoundError as file_error:
            return file_error

    return wrapper


def get_map():
    map = {}
    with open(data_dir / "map.json") as f:
        for line in json.load(f):
            map = map | line
    return map


@error_handler
def extract_from_json(path):
    return pd.read_json(path)


@error_handler
def extract_from_csv(path):
    return pd.read_csv(path)


def extract_from_xml(path):
    try:
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
    except ET.ParseError as parse_error:
        return parse_error
    except FileNotFoundError as file_error:
        return file_error


def extract_all(dir=(data_dir / "raw_data")):
    df = pd.DataFrame(columns=["car_model", "year_of_manufacture", "price", "fuel"])

    for file_pattern, func in get_map().items():
        filepaths = glob.glob(f"{dir}/{file_pattern}")
        for filepath in filepaths:
            new_df = eval(func)(filepath)
            df = pd.concat([df, new_df], ignore_index=True) if not df.empty else new_df

    return df
