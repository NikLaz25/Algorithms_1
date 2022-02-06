import unittest
from queue_1 import Queue

class MyTestCase(unittest.TestCase):
    def test_rotation(self):
        qu = Queue()
        qu.enqueue(1)
        qu.enqueue(2)
        qu.enqueue(3)
        qu.enqueue(4)
        qu.rotation(2)

        result = qu.LinkedList_in_List()
        answer = [3, 4, 1, 2]
        self.assertEqual(result, answer)

    def test_dequeue(self):
        qu = Queue()
        qu.enqueue(1)
        qu.enqueue(2)
        qu.enqueue(3)
        qu.enqueue(4)

        result = qu.dequeue()
        answer = 1
        self.assertEqual(result, answer)

    def test_size(self):
        qu = Queue()
        qu.enqueue(1)
        qu.enqueue(2)
        qu.enqueue(3)
        qu.enqueue(4)

        result = qu.size()
        answer = 4
        self.assertEqual(result, answer)
if __name__ == '__main__':
    unittest.main()
