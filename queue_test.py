import unittest
from queue_1 import Queue

class MyTestCase(unittest.TestCase):
    def test_rotation(self):
        '''тестируем rotation'''
        qu = Queue()
        qu.enqueue(1)
        qu.enqueue(2)
        qu.enqueue(3)
        qu.enqueue(4)
        qu.rotation(2)

        result = qu.LinkedList_in_List()
        answer = [3, 4, 1, 2]
        self.assertEqual(result, answer)

    def test_rotation_one(self):
        '''тестируем rotation когда элемент один в очереди'''
        qu = Queue()
        qu.enqueue(1)

        result = qu.LinkedList_in_List()
        answer = [1]
        self.assertEqual(result, answer)

    def test_rotation_none(self):
        '''тестируем rotation очередь пуста'''
        qu = Queue()

        result = qu.LinkedList_in_List()
        answer = []
        self.assertEqual(result, answer)

    def test_dequeue(self):
        '''тестируем dequeue'''
        qu = Queue()
        qu.enqueue(1)
        qu.enqueue(2)
        qu.enqueue(3)
        qu.enqueue(4)

        result = qu.dequeue()
        answer = 1
        self.assertEqual(result, answer)

    def test_dequeue_one(self):
        '''тестируем dequeue когда элемент один в очереди'''
        qu = Queue()
        qu.enqueue(1)

        result = qu.dequeue()
        answer = 1
        self.assertEqual(result, answer)

    def test_dequeue_one(self):
        '''тестируем dequeue когда очередь пуста'''
        qu = Queue()

        result = qu.dequeue()
        answer = None
        self.assertEqual(result, answer)

    def test_size(self):
        '''тестируем size'''
        qu = Queue()
        qu.enqueue(1)
        qu.enqueue(2)
        qu.enqueue(3)
        qu.enqueue(4)

        result = qu.size()
        answer = 4
        self.assertEqual(result, answer)

    def test_size(self):
        '''тестируем size когда элемент один в очереди'''
        qu = Queue()
        qu.enqueue(1)

        result = qu.size()
        answer = 1
        self.assertEqual(result, answer)

    def test_size(self):
        '''тестируем size когда очередь пуста'''
        qu = Queue()

        result = qu.size()
        answer = 0
        self.assertEqual(result, answer)

if __name__ == '__main__':
    unittest.main()
