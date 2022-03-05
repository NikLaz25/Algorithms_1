'''
Множества
'''


class PowerSet():
    '''Класс PowerSet наследует'''

    def __init__(self):
        '''Конструктор'''
        self.size_set = 30000
        self.step = 3
        self.slots = [None] * self.size_set

    def hash_fun(self, value):  # в качестве value поступают строки!
        '''по входному значению вычисляет индекс слота'''
        len_value = len(value)
        len_slots = len(self.slots)
        if len_value > len_slots:
            index = len_value - (len_value // len_slots) * len_slots - 1
        else:
            index = len_value - 1
        return index  # всегда возвращает корректный индекс слота

    def seek_slot(self, value):
        '''функцию поиска слота - по входному значению сперва рассчитывает индекс хэш-функцией,
        а затем отыскивает подходящий слот для него с учётом коллизий,
        или возвращает None, если это не удалось'''
        # находит индекс пустого слота для значения, или None
        index = self.hash_fun(value)
        len_slots = len(self.slots)
        if self.slots[index] is not None:
            check_slot_counter = 0
            while self.slots[index] is not None:
                check_slot_counter += 1
                if (index + 1 + self.step) <= len_slots and check_slot_counter < len_slots:
                    index += self.step
                elif (index + 1 + self.step) > len_slots and check_slot_counter < len_slots:
                    index = index + self.step - len(self.slots)
                elif check_slot_counter >= len_slots:
                    return None
        return index

    def find(self, value):
        '''проверяет, имеется ли в слотах указанное значение,
        и возвращает либо слот, либо None'''
        # находит индекс слота со значением, или None
        for index, val in enumerate(self.slots):
            if val == value:
                return index
        return None

    def size(self):
        '''количество элементов в множестве'''
        count = 0
        for element in self.slots:
            if element is not None:
                count += 1
        return count

    def put(self, value):
        '''помещает значение value в слот, вычисляемый с помощью функции поиска'''
        if self.find(value) is None:  # проверка наличия подобных значений
#             index = self.put_ht(value)
            index = self.seek_slot(value)
            if index is not None:
                self.slots[index] = value
                return index
        return

    def get(self, value):
        '''возвращает True если value имеется в множестве, иначе False'''
        for slot_value in self.slots:
            if slot_value == value:
                return True
        return False

    def remove(self, value):
        '''возвращает True если value удалено иначе False'''
        index = self.find(value)
        if index is not None:  # проверка наличия подобных значений
            self.slots[index] = None
        else:
            return False
        return True

    def intersection(self, set2):
        '''пересечение текущего множества и set2'''
        inter_set = []
        unique_set = list(set(set2))

        inter_set = [value for value in self.slots if value in unique_set and value is not None]

        return inter_set

    def union(self, set2):
        '''объединение текущего множества и set2'''
        union_set = []
        for value in self.slots:
            if value is not None:
                union_set += [value]

        for value in set2:
            index = self.find(value)
            if index is None and value is not None:  # проверка наличия значения value
                union_set += [value]
        return union_set

    def difference(self, set2):
        '''разница текущего множества и set2, то что не входит в set2'''
        dif_set = []
        for value in self.slots:
            if value is not None:
                count = 0
                for value2 in set2:
                    if value == value2:
                        count += 1
                if count == 0:
                    dif_set += [value]
        return dif_set

    def issubset(self, set2):
        '''возвращает True, если set2 есть подмножество
        текущего множества, иначе False'''
        count = 0
        for value2 in set2:
            for value in self.slots:
                if value2 == value and value is not None:
                    count += 1
        if count == len(set2):
            return True
        return False

    def print_slots(self):
        '''вспомогательный метод для печати списка без None'''
        result = [val for val in self.slots if val is not None]
        return result
