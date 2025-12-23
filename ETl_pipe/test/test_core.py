from src.core import *

data_dir = Path.cwd() / "data"


def test_module_export():
    assert bool(extract_all) is True


def test_extract_from_csv():
    wrong_file = data_dir / "raw_data/cars.json"
    missing_file = "missing_file.csv"
    assert isinstance(extract_from_csv(wrong_file), ValueError)
    assert isinstance(extract_from_csv(missing_file), FileNotFoundError)


def test_extract_from_json():
    wrong_file = data_dir / "raw_data/cars.csv"
    missing_file = "missing_file.json"
    assert isinstance(extract_from_json(wrong_file), ValueError)
    assert isinstance(extract_from_json(missing_file), FileNotFoundError)


def test_extract_from_xml():
    wrong_file = data_dir / "raw_data/cars.json"
    missing_file = "missing_file.xml"
    assert extract_from_xml(wrong_file), ET.ParseError
    assert isinstance(extract_from_xml(missing_file), FileNotFoundError)


def test_extractions(get_test_dir, fill_test_dir):
    populate_dir = fill_test_dir
    assert populate_dir is True

    dir = get_test_dir

    df = extract_all(dir)
    assert type(df) is pd.core.frame.DataFrame
