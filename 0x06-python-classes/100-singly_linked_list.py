#!/usr/bin/python3

"""Representing singly_linked_lists"""


class Node:
    """Class representing singly_linked_list"""

    def __init__(self, data, next_node=None):
        """Initializing new Node in program.

        Args:
            data (int): Data of the new node.
            next_node (Node): Next node in line.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """get & set data for_Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """get & set next_Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Representing a singly-linked_list."""

    def __init__(self):
        """Initalizing new_Singly-Linked-List."""
        self.__head = None

    def sorted_insert(self, value):
        """Inserting node in singly_linked_list.

        New node is inserted into the list

        Args:
            value (Node): New node inserted.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Defining print() singly_linked_list."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
