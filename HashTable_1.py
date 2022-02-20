class HashTable:
    def __init__(self, sz, stp):
        '''Конструктор'''
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value): # в качестве value поступают строки!
        '''по входному значению вычисляет индекс слота'''
        len_value = len(value)
        len_slots = len(self.slots)
        if len_value > len_slots:
            index = len_value - (len_value//len_slots) * len_slots -1
        else:
            index = len_value - 1
        return index # всегда возвращает корректный индекс слота

    def seek_slot(self, value):
        '''функцию поиска слота - по входному значению сперва рассчитывает индекс хэш-функцией,
        а затем отыскивает подходящий слот для него с учётом коллизий,
        или возвращает None, если это не удалось'''
         # находит индекс пустого слота для значения, или None
        index = self.hash_fun(value)
        len_slots = len(self.slots)
        if self.slots[index] is None:
            return index
        else:
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

    def put(self, value):
        '''помещает значение value в слот,
        вычисляемый с помощью функции поиска'''
        index = self.seek_slot(value)
        if index is None:
            return None
        else:
            self.slots[index] = value
        return index
        # записываем значение по хэш-функции возвращается индекс слота или None,
        # если из-за коллизий элемент не удаётся разместить

    def find(self, value):
        '''проверяет, имеется ли в слотах указанное значение,
        и возвращает либо слот, либо None'''
         # находит индекс слота со значением, или None
        for index in range(len(self.slots)):
            if self.slots[index] == value:
                return index
        return None