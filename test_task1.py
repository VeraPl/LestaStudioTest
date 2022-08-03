
from task1 import isEven
import pytest


def test_is_even():
    assert isEven(10)
    assert isEven(21) is False
    with pytest.raises(TypeError):
        isEven(4.98)
        isEven([])

