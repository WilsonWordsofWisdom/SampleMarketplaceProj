import pytest
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
def add_item(input):
    Items = Items()
    Items.add(input)
    assert Items.df.tail(1).to_dict('r') == input


def get_items(input):
    assert Items().get_items() == pd.read_csv('Products.csv')

