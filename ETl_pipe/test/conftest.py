import pytest
import csv
import pandas as pd


@pytest.fixture(scope="module")
def get_csv_file(tmpdir_factory):
    csv_file = tmpdir_factory.mktemp("data").join("csvNg.csv")
    headers = ["car_model", "year_of_manufacture", "price", "fuel"]
    with open(csv_file, "w") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerow(
            {
                "car_model": "Audi",
                "year_of_manufacture": 2000,
                "price": 3000,
                "fuel": "Diesel",
            }
        )
    return csv_file


@pytest.fixture(scope="module")
def get_test_df(get_csv_file):
    yield pd.read_csv(get_csv_file)
