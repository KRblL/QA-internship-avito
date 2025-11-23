import pytest
from create_item import CreateItem
from get_item_by_id import GetItemByID
from delete_item import DeleteItem
from data import *



@pytest.mark.parametrize("payload", [CREATE_VALID_PAYLOAD, CREATE_PAYLOAD_ZERO_STATISTICS])
def test_create_item_success(payload):
   new_item_endpoint = CreateItem()
   new_item_endpoint.new_item(payload=payload)
   assert new_item_endpoint.response.status_code == 200
   response_keys = set(new_item_endpoint.response_json.keys())
   expected_keys = {"id", "sellerId", "name", "price", "statistics", "createdAt"}
   assert response_keys == expected_keys

   get_item_endpoint = GetItemByID()
   get_item_endpoint.get_by_id(new_item_endpoint.get_item_id())
   assert get_item_endpoint.response.status_code == 200
   assert get_item_endpoint.response_json[0]["id"] == new_item_endpoint.get_item_id()

   delete_item_endpoint = DeleteItem()
   delete_item_endpoint.delete_by_id(new_item_endpoint.get_item_id())

def test_create_empty_json():
   new_item_endpoint = CreateItem()
   new_item_endpoint.new_item(payload={})
   assert new_item_endpoint.response.status_code == 400

def test_create_without_seller_id():
   new_item_endpoint = CreateItem()
   new_item_endpoint.new_item(payload=CREATE_PAYLOAD_WITHOUT_SELLERID)
   assert new_item_endpoint.response.status_code == 400

def test_create_without_name():
   new_item_endpoint = CreateItem()
   new_item_endpoint.new_item(payload=CREATE_PAYLOAD_WITHOUT_NAME)
   assert new_item_endpoint.response.status_code == 400

def test_create_without_price():
   new_item_endpoint = CreateItem()
   new_item_endpoint.new_item(payload=CREATE_PAYLOAD_WITHOUT_PRICE)
   assert new_item_endpoint.response.status_code == 400

def test_create_without_statistics():
   new_item_endpoint = CreateItem()
   new_item_endpoint.new_item(payload=CREATE_PAYLOAD_WITHOUT_STATISTICS)
   assert new_item_endpoint.response.status_code == 200

@pytest.mark.parametrize("payload", [p for p in CREATE_PAYLOAD_INVALID_SELLERID])
def test_create_invalid_sellerid(payload):
   new_item_endpoint = CreateItem()
   new_item_endpoint.new_item(payload)
   assert new_item_endpoint.response.status_code == 400

@pytest.mark.parametrize("payload", [p for p in CREATE_PAYLOAD_INVALID_NAME])
def test_create_invalid_name(payload):
   new_item_endpoint = CreateItem()
   new_item_endpoint.new_item(payload)
   assert new_item_endpoint.response.status_code == 400

@pytest.mark.parametrize("payload", [p for p in CREATE_PAYLOAD_INVALID_PRICE])
def test_create_invalid_price(payload):
   new_item_endpoint = CreateItem()
   new_item_endpoint.new_item(payload)
   assert new_item_endpoint.response.status_code == 400

@pytest.mark.parametrize("payload", [p for p in CREATE_PAYLOAD_INVALID_STATISTICS])
def test_create_invalid_statistics(payload):
   new_item_endpoint = CreateItem()
   new_item_endpoint.new_item(payload)
   assert new_item_endpoint.response.status_code == 400

def test_create_invalid_json():
   new_item_endpoint = CreateItem()
   new_item_endpoint.new_item(payload=CREATE_INVALID_PAYLOAD)
   assert new_item_endpoint.response.status_code == 400
