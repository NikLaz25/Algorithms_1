from typing import Any
from typing import Optional

class Node:

    def __init__(self, v: int) -> None:
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def add_in_tail(self, item: Optional[Node]) -> None:
        if self.head is None and self.tail is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item
        return None

    def print_all_nodes(self) -> None:
        node = self.head
        while node != None:
            print(node.value)
            node = node.next
        return None
    def len(self) -> int:
        node: Optional[Node] = self.head
        counter: int = 0
        while node is not None:
            counter += 1
            node = node.next
        return counter



def two_LinkedList(a_list: LinkedList, b_list: LinkedList) -> Optional[LinkedList]:
    '''метод который получает на вход два связанных списка,
    состоящие из целых значений, и если их длины равны,
    возвращает список, каждый элемент которого равен
    сумме соответствующих элементов входных списков'''
    node_a: Optional[Node] = a_list.head
    node_b: Optional[Node] = b_list.head
    s_list: LinkedList = LinkedList()
    node_last: Optional[Node] = None
    if a_list.len() != b_list.len():
        return None
    while node_a is not None:
        node: Optional[Node]  = s_list.add_in_tail(Node(node_a.value + node_b.value))
        if node_last is not None:
            node_last.next = node
        node_last = node
        node_a = node_a.next
        node_b = node_b.next

    return s_list.print_all_nodes()

# a_list = LinkedList()
# a_list.add_in_tail(Node(12))
# a_list.add_in_tail(Node(13))
# a_list.add_in_tail(Node(125))
# a_list.add_in_tail(Node(128))
#
# b_list = LinkedList()
# b_list.add_in_tail(Node(12))
# b_list.add_in_tail(Node(15))
# b_list.add_in_tail(Node(125))
# b_list.add_in_tail(Node(128))
#
#
# two_LinkedList(a_list, b_list)

