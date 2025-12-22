import pytest
import csv, json
import xml.etree.ElementTree as ET


def get_data():
    return {
        "car_model": "Audi",
        "year_of_manufacture": "2000",
        "price": "3000",
        "fuel": "Diesel",
    }


@pytest.fixture(scope="session")
def get_test_dir(tmp_path_factory):
    dir = tmp_path_factory.mktemp("data", numbered=False)
    if dir.exists():
        return dir


@pytest.fixture(scope="session")
def get_test_csv_file(get_test_dir):
    csv_file = get_test_dir / "test_file.csv"
    data = get_data()
    headers = data.keys()

    with open(csv_file, "w") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerow(data)

    return csv_file


@pytest.fixture(scope="session")
def get_test_json_file(get_test_dir):
    json_file = get_test_dir / "test_file.json"
    data = [get_data()]

    with open(json_file, "w") as file:
        json.dump(data, file)

    return json_file


@pytest.fixture(scope="session")
def get_test_xml_file(get_test_dir):
    xml_file = get_test_dir / "test_file.xml"
    data = get_data()
    root = ET.Element("cars")
    tree = ET.ElementTree(root)
    ver = ET.SubElement(root, "car")

    for k, v in data.items():
        ele = ET.SubElement(ver, k)
        ele.text = str(v)

    tree.write(open(xml_file, "wb"))

    return xml_file


@pytest.fixture(scope="session")
def fill_test_dir(get_test_csv_file, get_test_json_file, get_test_xml_file):

    files = [get_test_csv_file, get_test_json_file, get_test_xml_file]

    for file in files:
        get_file = file
        assert get_file.is_file() is True
    
    return True