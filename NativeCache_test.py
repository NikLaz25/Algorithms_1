import unittest
from NativeCache import NativeCache

class MyTestCase(unittest.TestCase):
    def test_put(self):
        '''Тестируем схему вытеснения'''
        size = 17
        my_instance = NativeCache(size)
        for x in range(17):
            key = str(x)
            value = x
            my_instance.put(key, value)
        for x in range(1, 17):
            key = str(x)
            my_instance.get(key)
        key, value = '125', 125
        my_instance.put(key, value)
        key, value = '127', 127
        my_instance.put(key, value)


        result = my_instance.slots
        answer = ['127', '6', '12', '1', '7', '13', '2', '8', '14', '3', '9', '15', '4', '10', '16', '5', '11']
        self.assertEqual(result, answer)
        result = my_instance.values
        answer = [127, 6, 12, 1, 7, 13, 2, 8, 14, 3, 9, 15, 4, 10, 16, 5, 11]
        self.assertEqual(result, answer)


if __name__ == '__main__':
    unittest.main()
