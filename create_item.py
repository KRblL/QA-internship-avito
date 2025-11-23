import requests
from base_endpoint import Endpoint


class CreateItem(Endpoint):
    item_id = None
    
    def new_item(self, payload):
        self.response = requests.post(
            url="https://qa-internship.avito.com/api/1/item",
            json=payload
        )
        if self.response.status_code == 200:
            self.response_json = self.response.json()
            self.item_id = self.response_json["status"].split(" - ")[1]
    
    def get_item_id(self):
        return getattr(self, "item_id", None)