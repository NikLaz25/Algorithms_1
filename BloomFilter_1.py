'''
фильтр Блюма, вариант 2
'''


class BloomFilter:
    '''Класс BloomFilter'''

    def __init__(self, f_len):
        '''создаём битовый массив длиной f_len '''
        self.filter_len = f_len
        self.bit_massiv = 0b10 ** self.filter_len

    def hash1(self, str1):
        '''hash1'''
        index = 0
        rand = 17
        for c in str1:
            code = ord(c)
            index = abs(index * rand + code)  # 223
            x = index // 32
            index = index - x * 32
        mask1 = 0b10 ** (32 - 1 - index)
        return mask1

    # выдаёт только одну, единственную позицию, индекс, в массиве
    # выдаёт битовую маску, в которой в позиции этого индекса выставлена единичка

    def hash2(self, str1):
        '''hash2'''
        index = 0
        rand = 223
        for c in str1:
            code = ord(c)
            index = abs(index * rand + code)  # 223
            x = index // 32
            index = index - x * 32
        mask2 = 0b10 ** (32 - 1 - index)
        return mask2

    def add(self, str1):
        '''добавляем строку str1 в фильтр'''
        self.bit_massiv = self.bit_massiv | self.hash1(str1)
        self.bit_massiv = self.bit_massiv | self.hash2(str1)

    def is_value(self, str1):
        '''проверка, имеется ли строка str1 в фильтре'''
        index1 = 31 - len(bin(self.hash1(str1))) + 3 + 3
        index2 = 31 - len(bin(self.hash2(str1))) + 3 + 3
        if bin(self.bit_massiv)[index1] == '1' and bin(self.bit_massiv)[index2] == '1':
            return True
        return False

