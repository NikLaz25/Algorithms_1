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
            if node.value is None:
                pass
            else:
                print(node.value)
            node = node.next
        return

    def clean(self):
        '''Очищаем список'''
        self.head = None
        self.tail = None
        return

    def len(self):
        '''Длина списка, метод скорректирован для фиктивных узлов'''
        node = self.head
        counter = 0
        while node is not None:
            if node.value is None:
                pass
            else:
                counter += 1
            node = node.next
        
        return counter
    def delete(self, val, all=False):
        '''Удалить значение, метод скорректирован для фиктивных узлов'''
        if self.head is None:  # Отрабатывает пустой список
            print('Отрабатывает пустой список')
            return None
#         параметры задаются после отработки пустого списка, т.к. иначе будет ошибка
        last_node = None
        node = self.head
        next_node = node.next


        if all is False:  # Если удаляем только один-первый найденный узел
            while node is not None:
                if node.value == val and node.next is not None:  # Удаляем число в середине
                    last_node.next = node.next
                    next_node.prev = node.prev
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
                if node.value == val and node.next is not None:  # Удаляем число в середине
                    last_node.next = node.next
                    next_node.prev = node.prev
                else:  # если ничего не удалили, только тогда левая граница - last_node двигается вправо
                    last_node = node

                node = node.next
                try:
                    next_node = node.next
                except:
                    pass
            return
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
                if node.value == afterNode.value and node != self.tail:  # когда нашли afterNode и когда он не последний
                    node.next = newNode
                    next_node.prev = newNode
                    newNode.next = next_node
                    newNode.prev = node
                    return

                node = node.next
                next_node = node.next

        elif afterNode is None and self.len() == 0:  # вставка в начало, в пустой список
            self.add_in_head(newNode)
            return None


        elif afterNode is None and self.len() != 0:  # вставка в конец, в непустой список
            self.add_in_tail(newNode)

        return
    
    def LinkedList_in_List(self):
        '''Вспомогательный метод для тестирования.
        Выводит значения связанного списка в обычный список'''
        node = self.head
        my_list = []
        while node is not None:
            my_list += [node.value]
            node = node.next
        return my_list