import unittest
from queue_2 import Deque

class MyTestCase(unittest.TestCase):
    def test_addFront(self):
        '''проверка addFront'''
        my_instance = Deque()
        my_instance.addFront(3)
        my_instance.addFront(4)
        my_instance.addFront(5)
        result = my_instance.print_list()
        answer = [5, 4, 3]
        self.assertEqual(result, answer)
        result_size = my_instance.size()
        answer_size = 3
        self.assertEqual(result_size, answer_size)

    def test_addTail(self):
        '''проверка addTail'''
        my_instance = Deque()
        my_instance.addTail(3)
        my_instance.addTail(4)
        my_instance.addTail(5)
        result = my_instance.print_list()
        answer = [3, 4, 5]
        self.assertEqual(result, answer)
        result_size = my_instance.size()
        answer_size = 3
        self.assertEqual(result_size, answer_size)

    def test_removeFront(self):
        '''проверка removeFront'''
        my_instance = Deque()
        my_instance.addTail(3)
        my_instance.addTail(4)
        my_instance.addTail(5)
        result = my_instance.removeFront()
        answer = 3
        self.assertEqual(result, answer)
        result_size = my_instance.size()
        answer_size = 2
        self.assertEqual(result_size, answer_size)

    def test_removeFront_1(self):
        '''проверка removeFront когда один узел'''
        my_instance = Deque()
        my_instance.addTail(3)
        result = my_instance.removeFront()
        answer = [3]
        self.assertEqual(result, answer)
        result_size = my_instance.size()
        answer_size = 0
        self.assertEqual(result_size, answer_size)

    def test_removeFront_0(self):
        '''проверка removeFront когда нет узлов'''
        my_instance = Deque()
        result = my_instance.removeFront()
        answer = None
        self.assertEqual(result, answer)
        result_size = my_instance.size()
        answer_size = 0
        self.assertEqual(result_size, answer_size)

    def test_removeTail(self):
        '''проверка removeTail'''
        my_instance = Deque()
        my_instance.addTail(3)
        my_instance.addTail(4)
        my_instance.addTail(5)
        result = my_instance.removeTail()
        answer = 5
        self.assertEqual(result, answer)
        result_size = my_instance.size()
        answer_size = 3
        self.assertEqual(result_size, answer_size)

    def test_removeTail_0(self):
        '''проверка removeTail когда нет узлов'''
        my_instance = Deque()
        result = my_instance.removeTail()
        answer = None
        self.assertEqual(result, answer)
        result_size = my_instance.size()
        answer_size = 0
        self.assertEqual(result_size, answer_size)

    def test_removeTail(self):
        '''проверка removeTail  когда один узел'''
        my_instance = Deque()
        my_instance.addTail(3)
        result = my_instance.removeTail()
        answer = 3
        self.assertEqual(result, answer)
        result_size = my_instance.size()
        answer_size = 1
        self.assertEqual(result_size, answer_size)

    def test_size(self):
        '''проверка size'''
        my_instance = Deque()
        my_instance.addTail(3)
        my_instance.addTail(4)
        my_instance.addTail(5)
        result = my_instance.size()
        answer = 3
        self.assertEqual(result, answer)





if __name__ == '__main__':
    unittest.main()
