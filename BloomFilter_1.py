'''
фильтр Блюма, вариант 1
'''


class BloomFilter:
    '''Класс BloomFilter'''

    def __init__(self, f_len):
        '''создаём битовый массив длиной f_len '''
        self.filter_len = f_len
        self.bit_massiv = '{:01b}'.format(0) * self.filter_len

    def hash1(self, str1):
        '''hash1'''
        result = 0
        rand = 17
        for c in str1:
            code = ord(c)
            result = abs(result * rand + code)  # 223
            x = result // 32
            result = result - x * 32
        return result

    # выдаёт только одну, единственную позицию, индекс, в массиве
    # выдаёт битовую маску, в которой в позиции этого индекса выставлена единичка

    def hash2(self, str1):
        '''hash2'''
        result = 0
        rand = 223
        for c in str1:
            code = ord(c)
            result = abs(result * rand + code)  # 223
            x = result // 32
            result = result - x * 32
        return result

    def add(self, str1):
        '''добавляем строку str1 в фильтр'''
        self.bit_massiv = self.bit_massiv[:self.hash1(str1)] + '1' + self.bit_massiv[self.hash1(str1) + 1:]
        self.bit_massiv = self.bit_massiv[:self.hash2(str1)] + '1' + self.bit_massiv[self.hash2(str1) + 1:]

    def is_value(self, str1):
        '''проверка, имеется ли строка str1 в фильтре'''
        hash_1 = int(self.hash1(str1))
        hash_2 = int(self.hash2(str1))
        if self.bit_massiv[hash_1] == '1' and self.bit_massiv[hash_2] == '1':
            return True
        return False