'''
Осваиваю очередь на основе двунаправленного связанного списка
'''

from typing import Optional


class Node:
    '''Класс Node определяет узел'''

    def __init__(self, v):
        '''Основной метод класса'''
        self.value = v
        self.prev = None
        self.next = None


class Queue:
    '''Класс Queue - очередь'''

    def __init__(self):
        '''инициализация хранилища данных'''
        self.head = None
        self.tail = None

    def enqueue(self, item):  # мера сложности О(1)
        '''Добавляем значение в список'''  # вставка в хвост
        item = Node(item)  # создаем узел
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item
        # return

    def dequeue(self) -> Optional[int]:  # мера сложности О(1)
        '''выдача из головы'''
        if self.head is None:
            return None  # если очередь пустая
        target = self.head
        self.head = self.head.next
        self.head.prev = None
        return target.value

    def size(self) -> int:  # мера сложности О(n)
        '''Размер'''
        node = self.head
        count = 0
        while node is not None:
            count += 1
            node = node.next
        return count  # размер очереди

    def print_all_nodes(self):
        '''Печать значений всех узлов'''
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next
        # return

    def rotation(self, quantity_elements: int):
        '''поворот очереди'''
        while quantity_elements > 0:
            self.enqueue(self.dequeue())
            quantity_elements -= 1

    def LinkedList_in_List(self):
        '''Вспомогательный метод для тестирования.
        Выводит значения связанного списка в обычный список'''
        node = self.head
        my_list = []
        while node is not None:
            my_list += [node.value]
            node = node.next
        return my_list