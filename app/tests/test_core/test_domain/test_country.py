import pytest
from app.src.core.domain import Country
from app.src.util import CountryEntity


@pytest.fixture()
def resource():
    countries = [
        CountryEntity({'languages': 'spa', 'region': u'América',
                       'name': u'Colombia'}),
        CountryEntity({'languages': 'spa', 'region': u'América',
                       'name': u'Chile'}),
        CountryEntity({'languages': 'spa', 'region': u'América',
                       'name': u'Perú'}),
        CountryEntity({'languages': 'spa', 'region': u'América',
                       'name': u'México'}),
    ]
    yield countries


class TestCountryDomain:
    def test_export_countries(self, resource, mocker):
        mocker.patch(
            'app.src.util.rest_countries.RestCountries.get_all_countries',
            return_value=resource
        )
        assert Country().export_countries()
