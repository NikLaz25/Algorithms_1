# Финальный вариант
class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.head
        find_list = []
        while node is not None:
            if node.value == val:
                find_list += [node]
            node = node.next
        return find_list # здесь будет ваш код

    def delete(self, val, all=False):
        last_node = None
        node = self.head

        if self.head is None: #Отрабатывает пустой список
            return None
        elif self.head == self.tail: #если в списке только один узел
            self.head = None
            self.tail = None
            return

        if all == False: #Если удаляем только один-первый найденный узел
            try:
                while node.value != val: # просматриваем список пока не будет найден элемент
                    last_node = node
                    node = node.next
            except:
                pass
            if last_node is None:# Удаляем только первый узел в списке
                self.head = self.head.next
                return

            elif node is None:# Прошлись по списку и не нашли нужного узла
                return  # возвращае всё без изменений

            elif node.next is None:# Удаляем только последний узел в списке
                last_node.next = None
                self.tail = last_node
                return
            else: # Удаляем узел из центра списка
                last_node.next = node.next
                return

        else:
            while node is not None:
                if self.head.value == val:
                    self.head = node.next
                elif node.value == val and node.next is not None: # Удаляем число в середине
                    last_node.next = node.next
                elif node.value == val and node.next is None: # Удаляем число в конце
                    last_node.next = None
                    self.tail = last_node
                else:
                    last_node = node
                node = node.next
            return

    def clean(self):
        self.head = None
        self.tail = None
        return

    def len(self):
        node = self.head
        counter = 0
        if  self.head is not None:
            while node is not None:
                counter += 1
                node = node.next
        return counter # здесь будет ваш код

    def insert(self, afterNode, newNode):
        node = self.head
        new_node = Node(newNode)
        if afterNode is not None:  # вставка после определенного значения
            while node is not None:
                last_node = node
                node = node.next
                if last_node.value == afterNode and last_node.value != self.tail.value:
                    new_node.next = last_node.next
                    last_node.next = new_node
                    return
                elif last_node.value == afterNode and last_node.value == self.tail.value:
                    new_node.next = last_node.next
                    last_node.next = new_node
                    self.tail = new_node
                    return
        elif afterNode is None and self.head is not None:  # вставка в начало, в непустой список
            second_node = self.head
            self.head = new_node
            node = new_node
            node.next = second_node

        elif afterNode is None and self.head is None:  # вставка в начало, в пустой список
            second_node = self.head
            self.head = new_node
            self.tail = new_node
            node = new_node
            node.next = second_node

    def LinkedList_in_List(self):
        '''Вспомогательный метод для тестирования. Выводит значения связанного списка в обычный список'''
        node = self.head
        my_list = []
        while node is not None:
            my_list += [node.value]
            node = node.next
        return my_list

