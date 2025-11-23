from get_item_by_id import GetItemByID
from data import *


def test_get_item_success(item_id):
   get_item_endpoint = GetItemByID()
   get_item_endpoint.get_by_id(item_id)
   assert get_item_endpoint.response.status_code == 200
   body = get_item_endpoint.response_json
   assert isinstance(body, list)
   assert len(body) == 1
   item = body[0]
   assert item["id"] == item_id

   assert "createdAt" in item
   assert item["createdAt"] is not None

   assert item["sellerId"] == CREATE_VALID_PAYLOAD["sellerID"]
   assert item["name"] == CREATE_VALID_PAYLOAD["name"]
   assert item["price"] == CREATE_VALID_PAYLOAD["price"]

   stats = item["statistics"]
   expected_stats = CREATE_VALID_PAYLOAD["statistics"]

   assert stats["likes"] == expected_stats["likes"]
   assert stats["viewCount"] == expected_stats["viewCount"]
   assert stats["contacts"] == expected_stats["contacts"]

def test_get_invalid_id():
   get_item_endpoint = GetItemByID()
   get_item_endpoint.get_by_id(GET_INVALID_ID)
   assert get_item_endpoint.response.status_code == 400

   assert "result" in get_item_endpoint.response_json
   assert "status" in get_item_endpoint.response_json
   assert get_item_endpoint.response_json["status"] == "400"

   assert "message" in get_item_endpoint.response_json["result"]
   assert "messages" in get_item_endpoint.response_json["result"]

def test_get_nonexistent_item():
   get_item_endpoint = GetItemByID()
   get_item_endpoint.get_by_id(GET_NON_EXISTENT_ID)
   assert get_item_endpoint.response.status_code == 404

   assert "result" in get_item_endpoint.response_json
   assert "status" in get_item_endpoint.response_json

   assert "message" in get_item_endpoint.response_json["result"]
   assert "messages" in get_item_endpoint.response_json["result"]

   assert get_item_endpoint.response_json["status"] == "404"
