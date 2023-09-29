#!/usr/bin/python3
"""
A singly linked list implementation
"""


class Node:
    """
    class:
        Node:  data, next_node=None
    method:
        ...
    """
    def __init__(self, data, next_node=None):
        if isinstance(data, int) is False:
            raise TypeError("data must be an integer")
        elif isinstance(next_node, Node) is False or next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.data

    @data.setter
    def data(self, value):
        if isinstance(value, int) is False:
            raise TypeError("data must be an integer")
        self.data = value

    @property
    def next_node(self):
        return self.next_node

    @next_node.setter
    def next_node(self, value):
        if isinstance(value, Node) is False:
            raise TypeError("next node must be a Node object")
        if value is not None or Node:
            raise TypeError("next_node must be a Node object")
        self.next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.head = []

    def sorted_inserted(self, value):
        sorted(self.head.append(value))
