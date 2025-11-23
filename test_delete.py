from delete_item import DeleteItem
from data import GET_INVALID_ID


def test_delete_by_id(item_id_for_delete):
   delete_item_endpoint = DeleteItem()
   delete_item_endpoint.delete_by_id(item_id_for_delete)
   assert delete_item_endpoint.response.status_code == 200
   delete_item_endpoint.delete_by_id(item_id_for_delete)
   assert delete_item_endpoint.response.status_code == 404
   delete_item_endpoint.delete_by_id(GET_INVALID_ID)
   assert delete_item_endpoint.response.status_code == 400
   