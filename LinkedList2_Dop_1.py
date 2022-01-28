'''
Работа со двунаправленным связанным списком
Дополнительное задание
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

    def __init__(self): #скорректировано для допзадания
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head


    def add_in_tail(self, item): #скорректировано для допзадания
        '''Добавляем значение в список'''
        afterNode = self.tail.prev
        newNode = item

        afterNode.next = newNode
        newNode.prev = afterNode
        newNode.next = self.tail
        self.tail.prev = newNode


    def print_all_nodes(self): #скорректировано для допзадания
        '''Печать значений всех узлов'''
        node = self.head
        while node is not None:
            if node.value is None:
                pass
            else:
                print(node.value)
            node = node.next

    def print_all_nodes_fict(self):  #скорректировано для допзадания
        '''Печать значений всех узлов включая фиктивные'''
        node = self.head
        while node is not None:
            if node.value is None:
                print(node, node.value)
            else:
                print(node.value)
            node = node.next

    def clean(self): #скорректировано для допзадания
        '''Очищаем список'''
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def len(self):  # скорректировано для допзадания
        '''Длина списка, метод скорректирован для фиктивных узлов'''
        node = self.head.next
        counter = 0
        while node is not None and node is not self.tail:
            if node.value is not None:
                counter += 1
            node = node.next

        return counter

    def delete(self, val, all = False):
        '''Удалить значение, метод скорректирован для фиктивных узлов'''
        last_node = None
        node = self.head
        next_node = node.next

        while node is not None and node.next is not None:
            if node.value == val:  # Удаляем число в середине
                last_node.next = node.next
                next_node.prev = node.prev
                if all is False:  # Если удаляем только один-первый найденный узел
                    return
            else:
                last_node = node
            node = node.next
            next_node = node.next

    def add_in_head(self, newNode):
        '''Добавляем значение в начало списка, метод скорректирован для фиктивных узлов'''
        second_node = self.head.next
        self.head.next = newNode
        newNode.next = second_node

    def insert(self, afterNode, newNode):
        '''Вставить значение, метод скорректирован для фиктивных узлов'''
        node = self.head

        if afterNode is not None:  # вставка после определенного значения
            next_node = node.next  # next_node поместил в это условие, т.к. с None оно не работает
            while node is not None:
                if node.value == afterNode.value:  # когда нашли afterNode
                    node.next = newNode
                    next_node.prev = newNode
                    newNode.next = next_node
                    newNode.prev = node
                    return

                node = node.next
                next_node = node.next

        elif afterNode is None:  # вставка когда afterNode is None
            self.add_in_tail(newNode)

    def LinkedList_in_List(self):
        '''Вспомогательный метод для тестирования.
        Выводит значения связанного списка в обычный список'''
        node = self.head
        my_list = []
        while node is not None:
            if node.value is not None:
                my_list += [node.value]
            node = node.next
        return my_list

    def find(self, val):
        '''Поиск значения в списке'''
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

# s_list = LinkedList2()
#
# s_list.add_in_tail(Node(10))
# s_list.add_in_tail(Node(20))
# s_list.add_in_tail(Node(10))
# nf = s_list.find(20)
# print(nf.value)

# s_list = LinkedList2()
#
# s_list.add_in_tail(Node(10))
# s_list.add_in_tail(Node(20))
# s_list.add_in_tail(Node(10))
# # s_list.add_in_tail(Node(20))
# # s_list.add_in_tail(Node(10))
# # s_list.add_in_tail(Node(20))
# # s_list.print_all_nodes()
# print(s_list.len())
# print(s_list.LinkedList_in_List())

# s_list = LinkedList2()
#
# s_list.add_in_tail(Node(10))
# s_list.add_in_tail(Node(20))
# s_list.add_in_tail(Node(10))
#
# s_list.delete(10, False)
# s_list.print_all_nodes()
# print(s_list.LinkedList_in_List())
#
#
# s_list.add_in_tail(Node(10))
# s_list.add_in_tail(Node(10))
# s_list.print_all_nodes()
#
# s_list.delete(10, True)
# print(s_list.LinkedList_in_List())
# s_list.print_all_nodes()