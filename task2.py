# -*- coding: utf-8 -*-
from collections import deque


class CycledBuffer1:
    """Реализация циклического буфера FIFO с помощью встроенного модуля  collections"""

    def __init__(self, size=10):
        self.value = None
        self.size = size
        self.buffer = deque()

    def append(self, value):
        self.value = value
        self.buffer.append(self.value)
        if len(self.buffer) > self.size:
            self.pop()

    def pop(self):
        if len(self.buffer):
            self.buffer.popleft()


class CycledBuffer2:
    """Реализация циклического буфера FIFO с помощью односвязного списка"""

    def __init__(self, maxsize=10):
        self.maxsize = maxsize
        self.node = None
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value):
        self.node = Node(value)
        if not self.head:
            self.head = self.node
        else:
            self.tail.next_node = self.node
        self.tail = self.node
        self.size += 1
        if self.size > self.maxsize:
            print self._pop()

    def _pop(self):
        value = self.head.value
        self.head = self.head.next_node
        self.size -= 1
        return "{0} was removed from the buffer".format(value)

    def get_list(self):
        node = self.head
        buffer = []
        while node:
            buffer.append(node.value)
            node = node.next_node
        return buffer


class Node:

    def __init__(self, value):
        self.next_node = None
        self.value = value
