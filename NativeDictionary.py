'''
Ассоциативный массив (словарь)
'''


class NativeDictionary:
    '''Класс ассоциативного массива'''
    def __init__(self, sz):
        '''конструктор'''
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):  # в качестве key поступают строки!
        '''по входному значению вычисляет индекс слота'''
        len_key = len(key)
        len_slots = len(self.slots)
        if len_key > len_slots:
            index = len_key - (len_key // len_slots) * len_slots - 1
        else:
            index = len_key - 1
        return index  # всегда возвращает корректный индекс слота

    def is_key(self, key):
        '''возвращает True если ключ имеется, иначе False'''
        for index in self.slots:
            if index == key:
                return True
        return False

    def put(self, key, value):
        '''гарантированно записываем значение value по ключу key'''
        index = self.seek_slot(key)
        my_key = self.is_key(key)
        if my_key is False:
            self.slots[index] = key
        self.values[index] = value

    def get(self, key):
        '''возвращает value для key, или None если ключ не найден'''
        for index, key_val in enumerate(self.slots):
            if key_val == key:
                return self.values[index]
        return None

    def seek_slot(self, value):
        '''функцию поиска слота - по входному значению сперва рассчитывает индекс хэш-функцией,
        а затем отыскивает подходящий слот для него с учётом коллизий,
        или возвращает None, если это не удалось'''
        # находит индекс пустого слота для значения, или None
        step = 3
        index = self.hash_fun(value)
        len_slots = len(self.slots)
        if self.slots[index] is None or self.slots[index] == value:
            return index
        else:
            check_slot_counter = 0
            while self.slots[index] is not None:
                check_slot_counter += 1
                if (index + 1 + step) <= len_slots and check_slot_counter < len_slots:
                    index += step
                elif (index + 1 + step) > len_slots and check_slot_counter < len_slots:
                    index = index + step - len(self.slots)
                elif check_slot_counter >= len_slots:
                    return None
        return index