import pytest
import pandas as pd
from offer import Offer

testdata = [
    ({
        'Product_ID': '1',
        'Buyer':'lauren',
        'Offer_Price': 1, 
        'Accepted': 0
    })
]

@pytest.mark.parametrize("input", testdata)
def test_add_offer(input):
    offer = Offer()
    offer.add(input, save=False)
    assert offer.df.tail(1).to_dict('r')[0] == input



