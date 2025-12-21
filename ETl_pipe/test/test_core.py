# run as 'python -m test.test' from the main directory because of relative import error.
from src.core import *


def test_module_export():
    assert bool(extract_all) is True


def test_extract_from_csv_1(get_test_csv_file):
    df = pd.read_csv(get_test_csv_file)
    assert type(df) is pd.core.frame.DataFrame


def test_extract_from_csv_2():
    json_file = data_dir / "raw_data/cars.json"
    missing_file = "missing_file.csv"
    assert isinstance(extract_from_csv(json_file), ValueError)
    assert isinstance(extract_from_csv(missing_file), FileNotFoundError)


def test_extract_from_json_1(get_test_json_file):
    df = pd.read_json(get_test_json_file)
    assert type(df) is pd.core.frame.DataFrame


def test_extract_from_json_2():
    csv_file = data_dir / "raw_data/cars.csv"
    missing_file = "missing_file.json"
    assert isinstance(extract_from_json(csv_file), ValueError)
    assert isinstance(extract_from_json(missing_file), FileNotFoundError)


def test_extract_from_xml_1(get_test_xml_file):
    df = extract_from_xml(get_test_xml_file)
    assert type(df) is pd.core.frame.DataFrame


def test_extract_from_xml_2():
    json_file = data_dir / "raw_data/cars.json"
    missing_file = "missing_file.xml"
    assert extract_from_xml(json_file), ET.ParseError
    assert isinstance(extract_from_xml(missing_file), FileNotFoundError)


def test_get_map():
    assert type(get_map()) is dict
