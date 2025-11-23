import pytest
from get_item_by_seller import GetItemBySellerID
from data import SELLER_ID2, INVALID_SELLER_ID


def test_get_items_by_seller_id_success(item_ids):
   get_item_endpoint = GetItemBySellerID()
   get_item_endpoint.get_by_seller_id(SELLER_ID2)

   assert get_item_endpoint.response.status_code == 200
   assert isinstance(get_item_endpoint.response_json, list), "Ожидался список объявлений"
   assert len(get_item_endpoint.response_json) == 3

   response_ids = {item.get("id") for item in get_item_endpoint.response_json}
   missing = item_ids - response_ids
   assert not missing, f"Не найдены объявления с id: {missing}"

   extra = response_ids - item_ids
   assert not extra, f"Ответ содержит лишние объявления: {extra}"

   for item in get_item_endpoint.response_json:
      assert item.get("sellerId") == SELLER_ID2, (
         f"Неверный sellerId у item {item.get("id")}: "
         f"ожидалось {SELLER_ID2}, получено {item.get("sellerId")}"
      )

def test_get_item_by_seller_id_success(item_id2):
    get_item_endpoint = GetItemBySellerID()
    get_item_endpoint.get_by_seller_id(SELLER_ID2)

    assert get_item_endpoint.response.status_code == 200
    assert isinstance(get_item_endpoint.response_json, list), "Ожидался список объявлений"
    assert len(get_item_endpoint.response_json) == 1, f"Ожидался 1 элемент, получено: {len(get_item_endpoint.response_json)}"

    item = get_item_endpoint.response_json[0]
    assert item.get("id") == item_id2, (
        f"Ожидался id={item_id2}, получено id={item.get("id")}"
    )

    assert item.get("sellerId") == SELLER_ID2, (
        f"Неверный sellerId: ожидалось {SELLER_ID2}, "
        f"получено {item.get("sellerId")}"
    )

def test_get_item_by_seller_id_empty():
   get_item_endpoint = GetItemBySellerID()
   get_item_endpoint.get_by_seller_id(SELLER_ID2)
   assert get_item_endpoint.response.status_code == 200
   assert isinstance(get_item_endpoint.response_json, list), "Ожидался список объявлений"
   assert len(get_item_endpoint.response_json) == 0, f"Ожидалось 0 элементов, получено: {len(get_item_endpoint.response_json)}"

@pytest.mark.parametrize("seller_id", [s for s in INVALID_SELLER_ID])
def test_get_item_by_invalid_seller_id(seller_id):
   get_item_endpoint = GetItemBySellerID()
   get_item_endpoint.get_by_seller_id(seller_id)
   assert get_item_endpoint.response.status_code == 400

   assert "result" in get_item_endpoint.response_json
   assert "status" in get_item_endpoint.response_json
   assert "message" in get_item_endpoint.response_json["result"]
   assert "messages" in get_item_endpoint.response_json["result"]
   assert get_item_endpoint.response_json["status"] == "400"