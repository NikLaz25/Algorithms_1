'''
метод суммирования двух связанных списков
'''

from typing import Optional

class Node:
    '''Класс Node'''

    def __init__(self, v: int):
        '''конструктор'''
        self.value = v
        self.next = None

class LinkedList:
    '''Класс LinkedList'''

    def __init__(self):
        '''конструктор'''
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def add_in_tail(self, item: Optional[Node]):
        '''вставка в хвост'''
        if self.head is None and self.tail is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item
        return

    def print_all_nodes(self):
        '''печать всего списка'''
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next
        return

    def len(self) -> int:
        '''длина списка'''
        node: Optional[Node] = self.head
        counter: int = 0
        while node is not None:
            counter += 1
            node = node.next
        return counter

def two_linkedlist(a_list: LinkedList, b_list: LinkedList) -> LinkedList:
    '''метод который получает на вход два связанных списка,
    состоящие из целых значений, и если их длины равны,
    возвращает список, каждый элемент которого равен
    сумме соответствующих элементов входных списков'''

    node_a: Node = a_list.head
    node_b: Node = b_list.head
    s_list: LinkedList = LinkedList()
    if a_list.len() != b_list.len():
        return s_list

    while node_a is not None:
        s_list.add_in_tail(Node(node_a.value + node_b.value))
        node_a = node_a.next
        node_b = node_b.next

    return s_list

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
# s_list = two_linkedlist(a_list, b_list)
# s_list.print_all_nodes()



