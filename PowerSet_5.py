'''
Множества
'''


class PowerSet():
    '''Класс PowerSet'''

    def __init__(self):
        '''Конструктор'''
        self.slots = {}

    def find(self, value):
        '''проверяет, имеется ли в слотах указанное значение,
        и возвращает либо слот, либо None'''
        find_val = self.slots.get(value)
        if find_val is not None:
            return find_val

    def size(self):
        '''количество элементов в множестве'''
        return len(self.slots)

    def put(self, value):
        '''помещает значение value в слот'''
        self.slots[value] = value

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
            self.slots.pop(index)
            return True
        return False

    def intersection(self, set2):
        '''пересечение текущего множества и set2'''
        inter_set = PowerSet()
        keys = self.slots
        for key in keys:
            if set2.get(key) is True:
                inter_set.put(key)
        return inter_set

    def union(self, set2):
        '''объединение текущего множества и set2'''
        union_set = PowerSet()
        for el in self.slots:
            union_set.put(el)
        for el in set2.slots:
            union_set.put(el)
        return union_set

    def difference(self, set2):
        '''разница текущего множества и set2, то что не входит в set2'''
        diff_set = PowerSet()
        for el in self.slots:
            if el not in set2.slots:
                diff_set.put(el)

        for el in set2.slots:
            if el not in self.slots:
                diff_set.put(el)

        return diff_set

    def issubset(self, set2):
        '''возвращает True, если set2 есть подмножество
        текущего множества, иначе False'''
        count = 0
        for value2 in set2.slots:
            if value2 in self.slots:
                count += 1
        if count == len(set2.slots):
            return True
        return False

