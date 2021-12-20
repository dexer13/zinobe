import time
import pathlib
import traceback
from typing import List, Dict

from app.src.core.util import DataStructure, RestCountries, Country, Encrypt


class CountryView:
    def export_countries(self) -> bool:
        try:
            countries: List[Country] = RestCountries.get_all_countries()
            countries_list: List[Dict] = \
                [self.__create_row(country) for country in countries]
            ds: DataStructure = DataStructure(countries_list)
            ds.to_json_file(f'app/tmp/json/data.json')
            ds.save_review()
            return True
        except Exception as e:
            print(traceback.format_exc())
            print(e)
            return False

    @staticmethod
    def __create_row(country: Country) -> Dict:
        start_time = time.time()
        data = dict()
        try:
            language = country.languages[0].get('name')
            data = {
                'region': country.region,
                'name': country.name,
                'language': Encrypt.easy_encrypt(language.encode('utf-8'))
            }
        finally:
            data['time'] = time.time() - start_time
            return data

