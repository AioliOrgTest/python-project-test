import pytest

@pytest.mark.parametrize("input_param", ["this is not a real test"])
def test_example(input_param):
    assert True 
