import unittest
from PowerSet import HashTable, PowerSet

class MyTestCase(unittest.TestCase):
    def test_atributs(self):
        '''тестируем получение атрибутов родительского класса'''
        size = 19
        step = 3
        exemplar = PowerSet()
        result = exemplar.slots
        answer = [None, None, None, None, None, None, None, None, None, None,\
                  None, None, None, None, None, None, None, None, None]
        self.assertEqual(result, answer)

    def test_put(self):
        '''тестируем put'''
        size = 19
        step = 3
        exemplar = PowerSet()
        val = '25'
        exemplar.put(val)
        result = exemplar.slots
        answer = [None, '25', None, None, None, None, None, None, None, None, \
                  None, None, None, None, None, None, None, None, None]
        self.assertEqual(result, answer)

        val = '25'
        exemplar.put(val)
        self.assertEqual(result, answer)

        val = '26'
        exemplar.put(val)
        result = exemplar.slots
        answer = [None, '25', None, None, '26', None, None, None, None, None,\
                  None, None, None, None, None, None, None, None, None]
        self.assertEqual(result, answer)

    def test_remove(self):
        '''тестируем remove'''
        size = 19
        step = 3
        exemplar = PowerSet()
        val = '25'
        exemplar.put(val)
        val = '26'
        exemplar.put(val)

        val = '26' # когда есть такой элемент
        exemplar.remove(val)
        result = exemplar.slots
        answer = [None, '25', None, None, None, None, None, None, None, None,\
                  None, None, None, None, None, None, None, None, None]
        self.assertEqual(result, answer)

        val = '27' # когда нет такого элемента
        exemplar.remove(val)
        self.assertEqual(result, answer)

        val = '25' # когда элемент последний
        exemplar.remove(val)
        result = exemplar.slots
        answer = [None, None, None, None, None, None, None, None, None, None,\
                  None, None, None, None, None, None, None, None, None]
        self.assertEqual(result, answer)

    def test_intersection(self):
        '''тестируем intersection'''
        size = 19
        step = 3
        exemplar = PowerSet()
        val = '25'
        exemplar.put(val)
        val = '26'
        exemplar.put(val)
        val = '125'
        exemplar.put(val)
        val = '1234'
        exemplar.put(val)
        val = '27'
        exemplar.put(val)

        set2 = ['25', '125', None]
        result = exemplar.intersection(set2)
        answer = ['25', '125']
        self.assertEqual(result, answer)

        set2 = ['251', '1251', None]
        result = exemplar.intersection(set2)
        answer = []
        self.assertEqual(result, answer)

    def test_union(self):
        '''тестируем union'''
        size = 19
        step = 3
        exemplar = PowerSet()
        val = '25'
        exemplar.put(val)
        val = '26'
        exemplar.put(val)
        val = '125'
        exemplar.put(val)
        val = '1234'
        exemplar.put(val)
        val = '27'
        exemplar.put(val)

        set2 = ['25', '124', None]
        result = exemplar.union(set2)
        answer = ['25', '125', '1234', '26', '27', '124']
        self.assertEqual(result, answer)

        set2 = []
        result = exemplar.union(set2)
        answer = ['25', '125', '1234', '26', '27']
        self.assertEqual(result, answer)

        size = 19
        step = 3
        exemplar = PowerSet(size, step)
        set2 = ['25', '124', None]
        result = exemplar.union(set2)
        answer = ['25', '124']
        self.assertEqual(result, answer)

    def test_difference(self):
        '''тестируем difference'''
        size = 19
        step = 3
        exemplar = PowerSet()
        val = '25'
        exemplar.put(val)
        val = '26'
        exemplar.put(val)
        val = '125'
        exemplar.put(val)
        val = '1234'
        exemplar.put(val)
        val = '27'
        exemplar.put(val)

        set2 = ['25', '125', None]
        result = exemplar.difference(set2)
        answer = ['1234', '26', '27']
        self.assertEqual(result, answer)

        set2 = ['25', '26', '125', '1234', '27']
        result = exemplar.difference(set2)
        answer = []
        self.assertEqual(result, answer)

    def test_issubset(self):
        '''тестируем issubset'''
        size = 19
        step = 3
        exemplar = PowerSet()
        val = '25'
        exemplar.put(val)
        val = '26'
        exemplar.put(val)
        val = '125'
        exemplar.put(val)
        val = '1234'
        exemplar.put(val)
        val = '27'
        exemplar.put(val)

        set2 = ['25', '27'] # все элементы параметра входят в текущее множество,
        result = exemplar.issubset(set2)
        answer = True
        self.assertEqual(result, answer)

        set2 = ['125', '271'] # не все элементы параметра входят в текущее множество)
        result = exemplar.issubset(set2)
        answer = False
        self.assertEqual(result, answer)

        set2 = ['25', '26', '125', '1234', '27', '28'] # все элементы текущего множества входят в параметр,
        result = exemplar.issubset(set2)
        answer = False
        self.assertEqual(result, answer)

    def test_get(self):
        '''тестируем get'''
        size = 19
        step = 3
        exemplar = PowerSet()
        val = '25'
        exemplar.put(val)
        val = '26'
        exemplar.put(val)
        val = '125'
        exemplar.put(val)
        val = '1234'
        exemplar.put(val)
        val = '27'
        exemplar.put(val)

        value = '27'
        result = exemplar.get(value)
        answer = True
        self.assertEqual(result, answer)

        value = '271'
        result = exemplar.get(value)
        answer = False
        self.assertEqual(result, answer)

    def test_size(self):
        '''тестируем size'''
        size = 19
        step = 3
        exemplar = PowerSet()
        val = '25'
        exemplar.put(val)
        val = '26'
        exemplar.put(val)
        val = '125'
        exemplar.put(val)
        val = '1234'
        exemplar.put(val)
        val = '27'
        exemplar.put(val)

        result = exemplar.size
        answer = 5
        self.assertEqual(result, answer)



if __name__ == '__main__':
    unittest.main()
