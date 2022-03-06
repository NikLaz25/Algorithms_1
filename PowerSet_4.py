'''
Множества
'''

class PowerSet():
    '''Класс PowerSet'''

    def __init__(self):
        '''Конструктор'''
        self.slots = {}
        self.set2 = {}

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

    def put2(self, value):
        '''помещает значение value в слот'''
        self.set2[value] = value

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
        inter_set = {}

        keys = self.slots
        for key in keys:
            if self.set2.get(key) is not None:
                inter_set[key] = key

        return inter_set

    def union(self, set2):
        '''объединение текущего множества и set2'''
        union_set = {}
        keys_set2 = self.set2.keys()
        for key in keys_set2:
            self.slots[key] = key
        return self.slots

    def difference(self, set2):
        '''разница текущего множества и set2, то что не входит в set2'''
        diff_set = {}
        for el in self.slots:
            if el in self.set2:
                diff_set[el] = el

        return diff_set

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
