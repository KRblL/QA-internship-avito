import pytest
from get_statistic_by_id import GetStatisticByID
from data import CREATE_VALID_PAYLOAD2, GET_INVALID_ID, GET_NON_EXISTENT_ID

@pytest.mark.parametrize("version", (1, 2))
def test_get_statistic_by_id_success(item_id2, version):
   get_statistic_endpoint = GetStatisticByID()
   get_statistic_endpoint.get_statistic_by_id(item_id2, version=version)
   assert get_statistic_endpoint.response.status_code == 200
   assert isinstance(get_statistic_endpoint.response_json, list)
   assert len(get_statistic_endpoint.response_json) == 1

   stats = get_statistic_endpoint.response_json[0]
   for field in ("likes", "viewCount", "contacts"):
      assert field in stats, f"В объекте статистики отсутствует поле '{field}'"

   assert stats["likes"] == CREATE_VALID_PAYLOAD2["statistics"]["likes"]
   assert stats["viewCount"] == CREATE_VALID_PAYLOAD2["statistics"]["viewCount"]
   assert stats["contacts"] == CREATE_VALID_PAYLOAD2["statistics"]["contacts"]

@pytest.mark.parametrize("version", (1, 2))
def test_get_statistic_by_invalid_id(version):
   get_statistic_endpoint = GetStatisticByID()
   get_statistic_endpoint.get_statistic_by_id(GET_INVALID_ID, version=version)

   assert get_statistic_endpoint.response.status_code == 400 if version == 1 else get_statistic_endpoint.response.status_code == 404
   assert "result" in get_statistic_endpoint.response_json
   assert "status" in get_statistic_endpoint.response_json
   assert get_statistic_endpoint.response_json["status"] == "400" if version == 1 else get_statistic_endpoint.response_json["status"] == "404"
   assert "message" in get_statistic_endpoint.response_json["result"]
   assert "messages" in get_statistic_endpoint.response_json["result"]

@pytest.mark.parametrize("version", (1, 2))
def test_get_statistic_by_nonexistent_id(version):
   get_statistic_endpoint = GetStatisticByID()
   get_statistic_endpoint.get_statistic_by_id(GET_NON_EXISTENT_ID, version=version)

   assert get_statistic_endpoint.response.status_code == 404
   assert "result" in get_statistic_endpoint.response_json
   assert "status" in get_statistic_endpoint.response_json
   assert get_statistic_endpoint.response_json["status"] == "404"
   assert "message" in get_statistic_endpoint.response_json["result"]
   assert "messages" in get_statistic_endpoint.response_json["result"]
