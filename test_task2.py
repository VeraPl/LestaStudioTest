from task2 import CycledBuffer1, CycledBuffer2
from collections import deque

def test_CycledBuffer1():
    cycle_buffer1 = CycledBuffer1(6)
    for i in range(6):
        cycle_buffer1.append(i)
    assert cycle_buffer1.buffer == deque([0, 1, 2, 3, 4, 5])
    cycle_buffer1.append(6)
    assert cycle_buffer1.buffer == deque([1, 2, 3, 4, 5, 6])
    cycle_buffer1.pop()
    assert cycle_buffer1.buffer == deque([2, 3, 4, 5, 6])
    assert CycledBuffer1().size is 10


def test_CycledBuffer2():
    cycle_buffer2 = CycledBuffer2(4)
    for i in range(4):
        cycle_buffer2.append(i)
    assert cycle_buffer2.get_list() == [0, 1, 2, 3]
    cycle_buffer2.append(None)
    assert cycle_buffer2.get_list() == [1, 2, 3, None]