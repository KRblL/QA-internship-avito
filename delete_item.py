import requests
from base_endpoint import Endpoint


class DeleteItem(Endpoint):
    def delete_by_id(self, id):
        self.response = requests.delete(
            url=f"https://qa-internship.avito.com//api/2/item/{id}"
        )
