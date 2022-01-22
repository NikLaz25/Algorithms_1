import unittest
from DynArray_1 import DynArray

class MyTestCase(unittest.TestCase):
    def test_insert_standart(self):
        '''Тестируем insert вставка элемента, когда в итоге размер буфера не превышен'''
        da = DynArray()
        da.append(0)
        da.append(1)
        da.append(2)
        da.insert(1, 5)
        da.insert(0, 5)
        da.insert(4, 5)
        da.insert(6, 7)
        result_list = da.array_in_list()
        answer_list = [5, 0, 5, 1, 5, 2, 7]
        self.assertEqual(result_list, answer_list)
        result_count = da.count
        answer_count = 7
        self.assertEqual(result_count, answer_count)
        result_capacity = da.capacity
        answer_capacity = 16
        self.assertEqual(result_capacity, answer_capacity)

    def test_insert_over_capacity(self):
        '''Тестируем insert вставка элемента, когда в итоге размер буфера превышен'''
        da = DynArray()
        for i in range(0, 16):
            da.append(i)

        da.insert(1, 5)
        result_list = da.array_in_list()
        answer_list = [0, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(result_list, answer_list)
        result_count = da.count
        answer_count = 17
        self.assertEqual(result_count, answer_count)
        result_capacity = da.capacity
        answer_capacity = 32
        self.assertEqual(result_capacity, answer_capacity)

    def test_capacity(self):
        '''Тестируем insert вставка элемента, корректное изменение размера буфера'''
        da = DynArray()
        for i in range(0, 17):
            da.append(i)
        da.insert(1, 5)
        result_capacity = da.capacity
        answer_capacity = 32
        self.assertEqual(result_capacity, answer_capacity)

        da = DynArray()
        for i in range(0, 33):
            da.append(i)
        da.insert(1, 5)
        result_capacity = da.capacity
        answer_capacity = 64
        self.assertEqual(result_capacity, answer_capacity)

        da = DynArray()
        for i in range(0, 65):
            da.append(i)
        da.insert(1, 5)
        result_capacity = da.capacity
        answer_capacity = 128
        self.assertEqual(result_capacity, answer_capacity)

    # def test_insert_exception(self):
    #     '''Тестируем insert попытка вставки элемента в недопустимую позицию'''
    #     da = DynArray()
    #     da.append(0)
    #     da.append(1)
    #     da.append(2)
    #     da.insert(10, 5)
    #
    #     result = da.array_in_list()
    #     answer = 'FAILED (errors=1)'
    #     self.assertEqual(result, answer)

    def test_delete_standart(self):
        '''удаление элемента, когда в результате размер буфера остаётся прежним (проверьте также размер буфера)'''
        da = DynArray()
        da.append(0)
        da.append(1)
        da.append(2)
        da.append(3)
        da.append(4)
        da.append(5)

        da.delete(0)
        da.delete(1)
        da.delete(3)

        result_list = da.array_in_list()
        answer_list = [1, 3, 4]
        self.assertEqual(result_list, answer_list)
        result_count = da.count
        answer_count = 3
        self.assertEqual(result_count, answer_count)
        result_capacity = da.capacity
        answer_capacity = 16
        self.assertEqual(result_capacity, answer_capacity)

    def test_delete_capacity(self):
        '''удаление элемента, когда в результате понижается
         размер буфера (проверьте также корректное изменение размера буфера)'''
        da = DynArray()
        for i in range(0, 17):
            da.append(i)
        result_capacity = da.capacity
        answer_capacity = 32
        self.assertEqual(result_capacity, answer_capacity)
        for i in range(2):
            da.delete(0)
        result_capacity = da.capacity
        answer_capacity = 21
        self.assertEqual(result_capacity, answer_capacity)
        result_list = da.array_in_list()
        answer_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        self.assertEqual(result_list, answer_list)

        da.delete(1)
        da.delete(1)
        da.delete(1)
        da.delete(1)
        da.delete(1)
        da.delete(1)
        result_capacity = da.capacity
        answer_capacity = 16
        self.assertEqual(result_capacity, answer_capacity)

        da.delete(1)
        da.delete(1)
        da.delete(1)
        result_capacity = da.capacity
        answer_capacity = 16
        self.assertEqual(result_capacity, answer_capacity)

        da = DynArray()
        for i in range(0, 33):
            da.append(i)
        result_capacity = da.capacity
        answer_capacity = 64
        self.assertEqual(result_capacity, answer_capacity)
        da.delete(0)
        da.delete(0)
        result_capacity = da.capacity
        answer_capacity = 42
        self.assertEqual(result_capacity, answer_capacity)

        for i in range(11):
            da.delete(0)
        result_capacity = da.capacity
        answer_capacity = 28
        self.assertEqual(result_capacity, answer_capacity)

        for i in range(7):
            da.delete(0)
        result_capacity = da.capacity
        answer_capacity = 18
        self.assertEqual(result_capacity, answer_capacity)

        for i in range(5):
            da.delete(0)
        result_capacity = da.capacity
        answer_capacity = 16
        self.assertEqual(result_capacity, answer_capacity)

        da = DynArray()
        for i in range(0, 65):
            da.append(i)
        result_capacity = da.capacity
        answer_capacity = 128
        self.assertEqual(result_capacity, answer_capacity)

        for i in range(2):
            da.delete(0)
        result_capacity = da.capacity
        answer_capacity = 85
        self.assertEqual(result_capacity, answer_capacity)

    # def test_insert_exception(self):
    #     '''Тестируем delete попытка удалить элемент из недопустимой позиции'''
    #     da = DynArray()
    #     da.append(0)
    #     da.append(1)
    #     da.append(2)
    #     da.delete(10)
    #
    #     result = da.array_in_list()
    #     answer = 'FAILED (errors=1)'
    #     self.assertEqual(result, answer)

if __name__ == '__main__':
    unittest.main()
