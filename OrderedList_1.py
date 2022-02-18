'''
Работа с упорядоченным списком
'''


class Node:
    '''Класс Node определяет узел'''
    def __init__(self, v):
        '''конструктор'''
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    '''Класс упорядоченного списка'''
    def __init__(self, asc):
        '''конструктор'''
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        '''метод сравнения значений'''
        if v1 < v2:  # -1 если v1 < v2
            return -1
        elif v1 == v2:  # 0 если v1 == v2
            return 0
        else:  # +1 если v1 > v2
            return 1

    def add(self, value):
        '''автоматическая вставка value в нужную позицию'''
        new_node = Node(value)
        node = self.head
        '''вставка в пустой список'''
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        '''если asc == True'''

        '''вставка в конец'''
        if new_node.value >= self.tail.value and self.__ascending is True:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.tail.next = None
            return

        '''вставка в середину'''
        if new_node.value >= self.head.value and self.__ascending is True:
            while self.compare(new_node.value, node.value) == 1 \
                    or self.compare(new_node.value, node.value) == 0 and node is not None:
                node = node.next
            node = node.prev
            new_node.next = node.next
            new_node.prev = node
            node.next.prev = new_node
            node.next = new_node
            return
        '''вставка в начало'''
        if new_node.value <= self.head.value and self.__ascending is True:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return

        '''если asc == False'''

        '''вставка в начало'''
        if new_node.value >= self.head.value and self.__ascending is False:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return

        '''вставка в конец'''
        if new_node.value <= self.tail.value and self.__ascending is False:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            return

        '''вставка в середину'''
        if new_node.value <= self.head.value and self.__ascending is False:
            while self.compare(new_node.value, node.value) == -1 \
                    or self.compare(new_node.value, node.value) == 0 and node is not None:
                node = node.next
            new_node.next = node
            new_node.prev = node.prev
            node.prev.next = new_node
            node.prev = new_node
            return

    def find(self,val):  # сложность в целом не поменялась О(n)
        # но есть вероятность более раннего прерывания цикла при node.value > val
        '''Поиск значения в списке'''
        node = self.head
        while node is not None and node.value <= val:  # обновлено по сравнению с обычным связанным списком
            if node.value == val:
                return node
            node = node.next
        return None  # здесь будет ваш код

    def delete(self, val):
        '''Поиск значения в списке'''
        node = self.head
        if self.head is None:  # если список пуст
            return
        if self.head == self.tail and self.head.value == val:  # удаление единственного значения
            self.head = None
            self.tail = None
            return
        if self.head.value == val:  # если нашли в начале
            self.head = self.head.next
            self.head.prev = None
            return
        if self.tail.value == val:  # если нашли в конце
            self.tail = self.tail.prev
            self.tail.next = None
            return
        # если нашли в середине
        while node is not None:
            if node.value == val:
                left_node = node.prev
                right_node = node.next
                left_node.next = right_node
                right_node.prev = left_node
                return
            node = node.next

    def clean(self, asc):
        '''метод очистка списка'''
        self.__ascending = asc
        self.head = None
        self.tail = None

    def len(self):
        '''Длина связанного списка'''
        node = self.head
        counter = 0
        if self.head is not None:
            while node is not None:
                counter += 1
                node = node.next
        return counter

    def get_all(self):
        '''метод получения списка узлов'''
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

    def LinkedList_in_List(self):
        '''Вспомогательный метод для тестирования.
        Выводит значения связанного списка в обычный список'''
        node = self.head
        my_list = []
        while node is not None:
            my_list += [node.value]
            node = node.next
        return my_list

    def print_all_nodes(self):
        '''Печать значений всех узлов'''
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next
        return


class OrderedStringList(OrderedList):
    '''Дочерний класс упорядоченного списка для работы со строками'''
    def __init__(self, asc):
        '''конструктор'''
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        ''' переопределённая версия метода compare для строк'''
        if v1[0] == ' ':
            v1 = v1[1:]
        if v1[-1] == ' ':
            v1 = v1[:-1]
        if v2[0] == ' ':
            v2 = v2[1:]
        if v2[-1] == ' ':
            v2 = v2[:-1]
        len_v1 = len(v1)
        len_v2 = len(v2)
        result = super().compare(len_v1, len_v2)
        return result