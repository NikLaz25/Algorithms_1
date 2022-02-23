import unittest
from NativeDictionary import NativeDictionary


class MyTestCase(unittest.TestCase):
    '''класс тестирования'''
    def test_slots_values(self):
        '''тестируем создание хэш таблицы'''
        size = 17
        my_instance = NativeDictionary(size)
        result_slots = my_instance.slots
        answer = [None, None, None, None, None, None, None,\
                  None, None, None, None, None, None, None, None, None, None]
        self.assertEqual(result_slots, answer)
        result_values = my_instance.values
        self.assertEqual(result_values, answer)

    def test_hash_fun(self):
        '''тестируем hash_fun'''
        size = 17
        my_instance = NativeDictionary(size)
        new_str = '123'
        result = my_instance.hash_fun(new_str)
        answer = 2
        self.assertEqual(result, answer)

    def test_is_key(self):
        '''тестируем is_key'''
        size = 17
        my_instance = NativeDictionary(size)

        key = '123'
        value = 123
        my_instance.put(key, value)

        result = my_instance.is_key(key)
        answer = True
        self.assertEqual(result, answer)

        key_2 = '124'
        result = my_instance.is_key(key_2)
        answer = False
        self.assertEqual(result, answer)

    def test_put(self):
        '''тестируем put'''
        size = 17
        my_instance = NativeDictionary(size)

        key = '123'
        value = 123
        my_instance.put(key, value)
        key = '124'
        value = 125
        my_instance.put(key, value)

        result_slots = my_instance.slots
        answer_slots = [None, None, '123', None, None, '124', None, None,
                        None, None, None, None, None, None, None, None, None]
        self.assertEqual(result_slots, answer_slots)
        result_values = my_instance.values
        answer_values = [None, None, 123, None, None, 125, None, None, None,
                         None, None, None, None, None, None, None, None]
        self.assertEqual(result_values, answer_values)

    def test_get(self):
        '''тестируем get извлечение значения по существующему ключу'''
        size = 17
        my_instance = NativeDictionary(size)

        key = '123'
        value = 123
        my_instance.put(key, value)
        key = '124'
        value = 125
        my_instance.put(key, value)

        result = my_instance.get(key)
        answer = 125
        self.assertEqual(result, answer)

    def test_get(self):
        '''тестируем get извлечение значения по отсутствующему ключу'''
        size = 17
        my_instance = NativeDictionary(size)

        key = '123'
        value = 123
        my_instance.put(key, value)
        key = '124'
        value = 125
        my_instance.put(key, value)
        key = '127'
        result = my_instance.get(key)
        answer = None
        self.assertEqual(result, answer)





if __name__ == '__main__':
    unittest.main()
