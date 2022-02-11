'''
Осваиваю двойную очередь на основе двунаправленного связанного списка
'''

class Node:
    '''Класс Node определяет узел'''

    def __init__(self, value):
        '''Основной метод класса'''
        self.value = value
        self.prev = None
        self.next = None

class Deque:
    '''Класс Queue - двусторонняя очередь'''
    def __init__(self):
        '''инициализация внутреннего хранилища'''
        self.head = None
        self.tail = None

    def addFront(self, item): # мера сложности О()
        '''добавление в голову'''
        item = Node(item)  # создаем узел
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            second = self.head
            self.head = item
            self.head.prev = None
            self.head.next = second
            second.prev = self.head

    def addTail(self, item): # мера сложности О()
        '''добавление в хвост'''
        item = Node(item)  # создаем узел
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def removeFront(self): # мера сложности О(1)
        '''удаление из головы'''
        if self.head is None: # если очередь пустая
            return None
        if self.head == self.tail: # когда элемент один в очереди
            target = self.head
            self.head = None
            return target.value
        target = self.head
        self.head = self.head.next
        self.head.prev = None
        return target.value

    def removeTail(self): # мера сложности О(1)
        '''удаление из хвоста'''
        if self.head is None: # если очередь пустая
            return None
        elif self.head == self.tail: # когда элемент один в очереди
            target = self.head
            self.head = None
            self.tail = None
            return target.value
        target = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        return target.value

    def size(self): # мера сложности О(n)
        '''размер очереди'''
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

    def LinkedList_in_List(self):
        '''Вспомогательный метод для тестирования.
        Выводит значения связанного списка в обычный список'''
        node = self.head
        my_list = []
        while node is not None:
            my_list += [node.value]
            node = node.next
        return my_list