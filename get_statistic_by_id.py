import requests
from base_endpoint import Endpoint


BASE_URL1 = f"https://qa-internship.avito.com/api/1/statistic"
BASE_URL2 = f"https://qa-internship.avito.com/api/2/statistic"


class GetStatisticByID(Endpoint):
    def get_statistic_by_id(self, item_id, version=1):
        base_url = f"{BASE_URL1}/{item_id}" if version == 1 else f"{BASE_URL2}/{item_id}"
        self.response = requests.get(
            url=base_url
        )
        self.response_json = self.response.json()