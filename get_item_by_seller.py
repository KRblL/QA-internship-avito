import requests
from base_endpoint import Endpoint


class GetItemBySellerID(Endpoint):
    def get_by_seller_id(self, seller_id):
        self.response = requests.get(
            url=f"https://qa-internship.avito.com//api/1/{seller_id}/item"
        )
        self.response_json = self.response.json()
        