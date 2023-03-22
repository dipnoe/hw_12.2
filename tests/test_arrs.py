import pytest

from utils import arrs


@pytest.fixture
def collection():
    return [1, 2, 3]


def test_get(collection):
    assert arrs.get(collection, 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice(collection):
    assert arrs.my_slice(collection, 1, 3) == [2, 3]
    assert arrs.my_slice(collection, 1) == [2, 3]
    assert arrs.my_slice(collection, -1) == [3]
    assert arrs.my_slice([], 1) == []
    assert arrs.my_slice(collection, -4) == [1, 2, 3]
