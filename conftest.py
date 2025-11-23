import pytest
from create_item import CreateItem
from delete_item import DeleteItem
from data import *


@pytest.fixture()
def item_id():
    create_item = CreateItem()
    create_item.new_item(payload=CREATE_VALID_PAYLOAD)
    id = create_item.get_item_id()
    yield id
    delete_item = DeleteItem()
    delete_item.delete_by_id(id)

@pytest.fixture()
def item_id2():
    create_item = CreateItem()
    create_item.new_item(payload=CREATE_VALID_PAYLOAD2)
    id = create_item.get_item_id()
    yield id
    delete_item = DeleteItem()
    delete_item.delete_by_id(id)

@pytest.fixture()
def item_id_for_delete():
    create_item = CreateItem()
    create_item.new_item(payload=CREATE_VALID_PAYLOAD)
    id = create_item.get_item_id()
    return id

@pytest.fixture()
def item_ids():
    create_item = CreateItem()
    create_item.new_item(payload=CREATE_VALID_PAYLOAD2)
    id1 = create_item.get_item_id()
    create_item.new_item(payload=CREATE_VALID_PAYLOAD2)
    id2 = create_item.get_item_id()
    create_item.new_item(payload=CREATE_VALID_PAYLOAD2)
    id3 = create_item.get_item_id()
    yield {id1, id2, id3}
    delete_item = DeleteItem()
    delete_item.delete_by_id(id1)
    delete_item.delete_by_id(id2)
    delete_item.delete_by_id(id3)