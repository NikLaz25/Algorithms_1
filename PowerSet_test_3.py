import unittest
from PowerSet import PowerSet

class MyTestCase(unittest.TestCase):
    def test_atributs(self):
        '''тестируем получение атрибутов родительского класса'''
        size = 19
        step = 3
        exemplar = PowerSet()
        result = exemplar.print_slots()
        answer = []
        self.assertEqual(result, answer)

    def test_put(self):
        '''тестируем put'''
        exemplar = PowerSet()
        val = '25'
        exemplar.put(val)
        result = exemplar.print_slots()
        answer = ['25']
        self.assertEqual(result, answer)

        val = '25'
        exemplar.put(val)
        result = exemplar.print_slots()
        self.assertEqual(result, answer)

        val = '26'
        exemplar.put(val)
        result = exemplar.print_slots()
        answer = ['25', '26']
        self.assertEqual(result, answer)

    def test_remove(self):
        '''тестируем remove'''
        exemplar = PowerSet()
        val = '25'
        exemplar.put(val)
        val = '26'
        exemplar.put(val)

        val = '26' # когда есть такой элемент
        exemplar.remove(val)
        result = exemplar.print_slots()
        answer = ['25']
        self.assertEqual(result, answer)

        val = '27' # когда нет такого элемента
        exemplar.remove(val)
        self.assertEqual(result, answer)

        val = '25' # когда элемент последний
        exemplar.remove(val)
        result = exemplar.print_slots()
        answer = []
        self.assertEqual(result, answer)

    def test_intersection(self):
        '''тестируем intersection'''
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

        set2 = ['25', '25', '27', '125', '1234', None, '123']
        result = exemplar.intersection(set2)
        answer = ['25', '125', '1234', '27']
        self.assertEqual(result, answer)

    def test_union(self):
        '''тестируем union'''
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
        answer = ['25', '26', '125', '1234', '27', '124']
        self.assertEqual(result, answer)

        set2 = []
        result = exemplar.union(set2)
        answer = ['25', '26', '125', '1234', '27']
        self.assertEqual(result, answer)
        #
        # size = 19
        # step = 3
        exemplar = PowerSet()
        set2 = ['25', '124', None]
        result = exemplar.union(set2)
        answer = ['25', '124']
        self.assertEqual(result, answer)

    def test_difference(self):
        '''тестируем difference'''
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

        result = exemplar.size()
        answer = 5
        self.assertEqual(result, answer)

        exemplar = PowerSet()
        for value in range(100):
            exemplar.put(str(value))

        result = exemplar.size()
        answer = 100
        self.assertEqual(result, answer)



if __name__ == '__main__':
    unittest.main()
