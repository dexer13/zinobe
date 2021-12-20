import pytest
import pathlib
import json
from app.src.util.data_structure import DataStructure

@pytest.fixture()
def resource():
    info: list = [
        {'Region': u'América', 'Country_Name': u'Colombia', 'time': 0.5},
        {'Region': u'América', 'Country_Name': u'Chile', 'time': 1},
        {'Region': u'América', 'Country_Name': u'Perú', 'time': 3},
        {'Region': u'América', 'Country_Name': u'México', 'time': 2},
    ]
    yield info


class TestDataStructure:

    def test_to_json_file(self, resource):
        data_structure: DataStructure = DataStructure(resource)
        file_path: str = f'{pathlib.Path(__file__).parent.absolute()}' \
                         f'/data.json'
        data_structure.to_json_file(file_path)
        file = open(file_path)
        data = json.load(file)
        assert len(data) == 4

    def test_get_review(self, resource):
        data_structure: DataStructure = DataStructure(resource)
        review: DataStructure = data_structure.get_review()
        assert review.data_frame.iloc[0]['time'] == 6.5

    def test_save(self, resource):
        data_structure: DataStructure = DataStructure(resource)
        review: DataStructure = data_structure.get_review()
        result = review.save()
        assert result
