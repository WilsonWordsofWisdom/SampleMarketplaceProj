import pytest
from users import Users

testdata = [
    ({
        'Username': 'lauren',
        'Email': 'lauren@sample.com.sg',
        'Password': '1234'
    })
]

@pytest.mark.parametrize('input', testdata)
def test_register(input):
    users = Users()
    users.register(input)
    assert users.df.tail(1).to_dict('r')[0] == input
