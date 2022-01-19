import ctypes


class DynArray:
    '''Класс динамических массивов'''

    def __init__(self):
        '''Конструктор атрибутов экземпляра класса'''
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        '''Длина массива'''
        return self.count

    def make_array(self, new_capacity):
        '''Бронирование ячейки памяти'''
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        '''Проверка корректности индекса'''
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        '''Увеличение размера буфера для массива с сохранением элементов'''
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):  # сложность О(1)
        '''Добавление элемента в конец массива'''
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def help_check(self, i, itm):
        '''Вспомогательный метод для проверки вставки по индексу'''
        self.array[i] = itm
        if (i + 1) > self.count:
            self.count += 1
        return None

    def print_attributes(self):
        '''Вспомогательный метод равспечатки атрибутов экземпляра класса'''
        print('self.count: ', da.count, '\n', \
              'self.capacity: ', da.capacity, '\n', \
              'self.array: ', da.array)
        return None

    def insert(self, i, itm):  # сложность О(n)
        '''Вставка нового объекта по индексу'''  # добавляем объект itm в позицию i, начиная с 0

        '''Отработка исключений'''
        if i < 0 or i > self.count:  # сложность О(1)
            raise IndexError('Index is out of bounds')

        '''Увеличение ёмкости, при необходимости'''
        if self.count == self.capacity:  # сложность О(1)
            self.resize(2 * self.capacity)

        '''Вариант вставки в справа'''
        if i == self.count:  # сложность О(1)
            self.append(itm)
            return None

        '''Сдвиг объектов справа'''
        for j in range(i, self.__len__())[::-1]:  # сложность О(n)
            self.array[j + 1] = self.array[j]
            if (j + 2) > self.count:
                self.count += 1
        self.array[i] = itm

        return None

    def delete(self, i):  # сложность О(n) т.к. присутствует цикл
        '''Удаляем объект в позиции i'''

        '''Отработка исключений'''
        self.__getitem__(i)

        '''Сдвиг объектов справа от указанного, на один шаг влево'''
        for j in range(i, self.count - 1):
            self.array[j] = self.array[j + 1]
        self.count -= 1

        '''Уменьшение ёмкости, при необходимости'''
        if self.capacity / 2 >= self.count and self.capacity > 16:
            self.resize(int(self.capacity / 2))

        return None

    def print_array(self):
        '''Вспомогательный метод печати массива'''
        i = 0
        while i < self.__len__():
            print(i, self.__getitem__(i))
            i += 1
        return None

    def array_in_list(self):
        '''Вспомогательные метод для выведения массива в список'''
        array_list = []
        for i in range(0, self.count):
            array_list += [self.__getitem__(i)]
        return array_list

# da = DynArray()
# da.append(0)
# da.append(1)
# da.append(2)
# da.append(3)
# da.append(4)
#
# da.print_array()
# da.print_attributes()
#
# da.delete(5)
#
# da.print_array()
# da.print_attributes()

