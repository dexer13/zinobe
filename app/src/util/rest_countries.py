from restcountries import RestCountryApiV2 as rapi
from typing import List
from restcountries.base import Country


class RestCountries:
    @staticmethod
    def get_all_countries() -> List[Country]:
        countries: List = rapi.get_all()
        return countries
