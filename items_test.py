import pytest
import pandas as pd
from items import Items
testdata = [
    ({
        'Title': 'test Item',
        'Description': 'testing',
        'Price': '100', 
        'Quantity':'1',
        'Seller':'lauren',
    })
]

@pytest.mark.parametrize("input", testdata)
def test_add_item(input):
    items = Items()
    items.add(input)
    assert items.df.tail(1).to_dict('r')[0] == input

@pytest.mark.parametrize("input", testdata)
def test_get_items(input):
    assert Items().get_items().to_dict() == pd.read_csv('Products.csv').to_dict()


