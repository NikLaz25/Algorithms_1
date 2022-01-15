'''
Работа со двунаправленным связанным списком
'''


class Node:
    '''Класс Node определяет узел'''

    def __init__(self, v):
        '''Основной метод класса'''
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    '''Класс задаёт связанный список'''

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        '''Добавляем значение в список'''
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item
        return

    def print_all_nodes(self):
        '''Печать значений всех узлов'''
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next
        return

    def find(self, val):
        '''Поиск значения в списке'''
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        '''Поиск всех значений в списке'''
        node = self.head
        find_list = []
        while node is not None:
            if node.value == val:
                find_list += [node]
            node = node.next
        return find_list

    def delete(self, val, all=False):
        '''Удалить значение'''
        if self.head is None:  # Отрабатывает пустой список
            return None
        # параметры задаются после отработки пустого списка, т.к. иначе будет ошибка
        last_node = None
        node = self.head
        next_node = node.next

        if self.head == self.tail:  # если в списке только один узел
            self.head = None
            self.tail = None
            return

        if all is False:  # Если удаляем только один-первый найденный узел
            while node is not None:
                if self.head.value == val:
                    self.head = node.next
                    self.head.prev = None
                    next_node.prev = None
                    return
                elif node.value == val and node.next is not None:  # Удаляем число в середине
                    last_node.next = node.next
                    next_node.prev = node.prev
                    return
                elif node.value == val and node.next is None:  # Удаляем число в конце
                    last_node.next = None
                    self.tail = last_node
                    return
                last_node = node
                node = node.next
                try:
                    next_node = node.next
                except:
                    pass
            return

        else:
            while node is not None:
                if self.head.value == val:
                    self.head = node.next
                    self.head.prev = None
                    next_node.prev = None
                elif node.value == val and node.next is not None:  # Удаляем число в середине
                    last_node.next = node.next
                    next_node.prev = node.prev
                elif node.value == val and node.next is None:  # Удаляем число в конце
                    last_node.next = None
                    self.tail = last_node

                else:  # если ничего не удалили, только тогда левая граница - last_node двигается вправо
                    last_node = node

                node = node.next
                try:
                    next_node = node.next
                except:
                    pass
            return

    def clean(self):
        '''Очищаем список'''
        self.head = None
        self.tail = None
        return

    def len(self):
        '''Длина списка'''
        node = self.head
        counter = 0
        if self.head is not None:
            while node is not None:
                counter += 1
                node = node.next
        return counter

    def insert(self, afterNode, newNode):
        '''Вставить значение'''
        node = self.head

        if afterNode is not None:  # вставка после определенного значения
            next_node = node.next  # next_node поместил в это условие, т.к. с None оно не работает
            while node is not None:
                if node.value == afterNode.value and node != self.tail:  # когда нашли afterNode и когда он не последний
                    node.next = newNode
                    next_node.prev = newNode
                    newNode.next = next_node
                    newNode.prev = node
                    return
                if node.value == afterNode.value and node == self.tail:  # когда нашли afterNode и он последний
                    node.next = newNode
                    newNode.next = None
                    newNode.prev = node
                    self.tail = newNode
                    return
                node = node.next
                next_node = node.next

        elif afterNode is None and self.head is None:  # вставка в начало, в пустой список
            self.head = newNode
            self.tail = newNode
            node = newNode
            node.next = None
            node.prev = None

        elif afterNode is None and self.head is not None:  # вставка в конец, в непустой список
            self.tail.next = newNode
            newNode.prev = self.tail
            newNode.next = None
            self.tail = newNode

        return

    def add_in_head(self, newNode):
        '''Добавляем значение в начало списка'''
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            second_node = self.head
            self.head.prev = newNode
            self.head = newNode
            self.head.next = second_node


    def LinkedList_in_List(self):
        '''Вспомогательный метод для тестирования.
        Выводит значения связанного списка в обычный список'''
        node = self.head
        my_list = []
        while node is not None:
            my_list += [node.value]
            node = node.next
        return my_list