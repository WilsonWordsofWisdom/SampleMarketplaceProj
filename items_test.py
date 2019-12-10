import pytest
from items import Items
testdata = [
    ('',{'name': {0: 'book', 1: 'ipad'}, 'price': {0: '1', 1: 4}}),
]


@pytest.mark.parametrize("input, output", testdata)
def get_items(input, output):
    assert Items().get_items().to_dict() == output


@pytest.mark.parametrize("input, output", testdata)
def get_items(input, output):
    assert Items().add().to_dict() == output