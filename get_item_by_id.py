import requests
from base_endpoint import Endpoint


class GetItemByID(Endpoint):
    def get_by_id(self, item_id):
        self.response = requests.get(
            url=f"https://qa-internship.avito.com/api/1/item/{item_id}"
        )
        self.response_json = self.response.json()
        