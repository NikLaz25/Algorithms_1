'''
Множества
'''


class HashTable:
    '''Родительский класс Хэш-таблиц'''


    def find(self, value):
        '''проверяет, имеется ли в слотах указанное значение,
        и возвращает либо слот, либо None'''
        # находит индекс слота со значением, или None
        for index in range(len(self.slots)):
            if self.slots[index] == value:
                return index
        return None


class PowerSet(HashTable):
    '''Дочерний класс PowerSet наследует методы класса HashTable
    реализация хранилища'''

    def __init__(self):
        '''Конструктор'''
        self.slots = []

    def size(self):
        '''количество элементов в множестве'''
        count = 0
        for element in self.slots:
            if element is not None:
                count += 1
        return count

    def put(self, value):
        '''помещает значение value в слот'''
        if self.find(value) is None:  # проверка наличия подобных значений
            self.slots += [value]
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
            self.slots.pop(index)
            return True
        else:
            return False

    def intersection(self, set2):
        '''пересечение текущего множества и set2'''
        inter_set = []
        unique_set = list(set(set2))

        inter_set = [value for value in self.slots if value in unique_set]

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
                if value2 == value and value != None:
                    count += 1
        if count == len(set2):
            return True
        else:
            return False

