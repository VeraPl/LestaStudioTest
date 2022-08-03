from task3 import quick_sort
from random import sample
import pytest

def test_task3():
    assert quick_sort([]) == []
    assert quick_sort([0]) == [0]
    numbers = [i for i in sample(range(0, 5000), 10)]
    assert quick_sort(numbers) == sorted(numbers)
    numbers1 = [i for i in sample(range(0, 10000), 1500)]
    assert quick_sort(numbers1) == sorted(numbers1)
    with pytest.raises(TypeError):
        assert quick_sort(4)
        assert quick_sort("Test")
        assert quick_sort(None)

