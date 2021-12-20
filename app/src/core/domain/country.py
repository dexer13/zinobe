import time
from typing import List, Dict

from app.src.util import DataStructure, RestCountries, CountryEntity, Encrypt


class Country:
    def export_countries(self) -> bool:
        try:
            countries: List[CountryEntity] = RestCountries.get_all_countries()
            countries_list: List[Dict] = \
                [self.__create_row(country) for country in countries]
            ds: DataStructure = DataStructure(countries_list)
            ds.to_json_file(f'app/tmp/json/data.json')
            review: DataStructure = ds.get_review()
            review.save()
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def __create_row(country: CountryEntity) -> Dict:
        start_time = time.time()
        data = dict()
        try:
            language = country.languages[0].get('name')
            data = {
                'Region': country.region,
                'Country Name': country.name,
                'Language': Encrypt.easy_encrypt(language)
            }
        finally:
            data['time'] = time.time() - start_time
            return data

