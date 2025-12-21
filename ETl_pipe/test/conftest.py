import pytest
import pandas as pd
import csv
import json
from dicttoxml import dicttoxml


def get_data():
    return {
        "car_model": "Audi",
        "year_of_manufacture": 2000,
        "price": 3000,
        "fuel": "Diesel",
    }


@pytest.fixture(scope="module")
def get_csv_file(tmpdir_factory):
    csv_file = tmpdir_factory.mktemp("data").join("test_file.csv")
    data = get_data()
    headers = data.keys()
    with open(csv_file, "w") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerow(data)
    return csv_file


@pytest.fixture(scope="module")
def get_test_df_from_csv(get_csv_file):
    yield pd.read_csv(get_csv_file)


@pytest.fixture(scope="module")
def get_json_file(tmpdir_factory):
    json_file = tmpdir_factory.mktemp("data").join("test_file.json")
    data = list(get_data())
    with open(json_file, "w") as file:
        json.dump(data, file)
    return json_file


@pytest.fixture(scope="module")
def get_test_df_from_json(get_json_file):
    yield pd.read_json(get_json_file)


# @pytest.fixture(scope="module")
# def get_xml_file(tmpdir_factory):
#     xml_file = tmpdir_factory.mktemp("data").join("test_file.xml")
#     data = get_data()
#     xml_data = dicttoxml({"car": data}, custom_root="cars")
#     with open(xml_file, "wb") as file:
#         file.write(xml_data)
#     print(type(xml_file))
#     return xml_file



# @pytest.fixture(scope="module")
# def get_test_df_from_xml(get_xml_file):
#     yield pd.read_xml(get_xml_file)
