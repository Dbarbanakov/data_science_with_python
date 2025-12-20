# run as 'python -m test.test' from the main directory because of relative import error.
from src.core import *


def test_module_export():
    assert bool(extract_all) == True


def test_extract_from_csv_1(get_test_df):
    df1 = extract_from_csv((data_dir / "raw_data/cars.csv"))
    df2 = get_test_df
    assert type(df1) == type(df2)


def test_extract_from_csv_2():
    json_file = data_dir / "raw_data/cars.json"
    missing_file = data_dir / "raw_data/missing_file.csv"
    assert isinstance(extract_from_csv(json_file), ValueError)
    assert isinstance(extract_from_csv(missing_file), FileNotFoundError)


def test_extract_from_json_2():
    csv_file = data_dir / "raw_data/cars.csv"
    missing_file = data_dir / "raw_data/missing_file.json"
    assert isinstance(extract_from_json(csv_file), ValueError)
    assert isinstance(extract_from_json(missing_file), FileNotFoundError)
