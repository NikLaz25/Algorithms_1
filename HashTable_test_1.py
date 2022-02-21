import unittest
from HashTable_1 import HashTable


class MyTestCase(unittest.TestCase):
    def test_HashTable(self):
        '''тестируем создание хэш таблицы'''
        size = 17
        step = 3
        my_instance = HashTable(size, step)
        result = my_instance.slots
        answer = [None, None, None, None, None, None, None, None, None,\
                  None, None, None, None, None, None, None, None]
        self.assertEqual(result, answer)

    def test_hash_fun(self):
        '''тестируем hash_fun'''
        size = 17
        step = 3
        my_instance = HashTable(size, step)
        new_str = '123'
        result = my_instance.hash_fun(new_str)
        answer = 2
        self.assertEqual(result, answer)

        new_str = '123456789012345678'
        result = my_instance.hash_fun(new_str)
        answer = 0
        self.assertEqual(result, answer)

    def test_seek_slot(self):
        '''тестируем seek_slot'''
        size = 17
        step = 3
        my_instance = HashTable(size, step)
        my_instance.slots[0] = '123'
        new_str = '123456789012345678'
        result = my_instance.seek_slot(new_str)
        answer = 3
        self.assertEqual(result, answer)

        my_instance.slots[0] = '123'
        new_str = '123'
        result = my_instance.seek_slot(new_str)
        answer = 2
        self.assertEqual(result, answer)

    def test_seek_put(self):
        '''тестируем put'''
        size = 17
        step = 3
        my_instance = HashTable(size, step)
        my_instance.slots[0] = '123'
        new_str = '123456789012345678'
        my_instance.put(new_str)
        result = my_instance.slots
        answer = ['123', None, None, '123456789012345678', None, None, None,\
                  None, None, None, None, None, None, None, None, None, None]
        self.assertEqual(result, answer)

        size = 17
        step = 3
        my_instance = HashTable(size, step)
        my_instance.slots[0] = '123'
        new_str = '321'
        my_instance.put(new_str)
        result = my_instance.slots
        answer = ['123', None, '321', None, None, None, None, None, None, None,
                  None, None, None, None, None, None, None]
        self.assertEqual(result, answer)

    def test_find(self):
        '''тестируем find'''
        size = 17
        step = 3
        my_instance = HashTable(size, step)
        my_instance.slots[0] = '123'
        new_str = '123456789012345678'
        my_instance.put(new_str)
        result = my_instance.find(new_str)
        answer = 3
        self.assertEqual(result, answer)

        size = 17
        step = 3
        my_instance = HashTable(size, step)
        my_instance.slots[0] = '123'
        new_str = '321'
        my_instance.put(new_str)
        result = my_instance.find(new_str)
        answer = 2
        self.assertEqual(result, answer)

if __name__ == '__main__':
    unittest.main()
