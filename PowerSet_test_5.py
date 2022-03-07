import unittest
from PowerSet_5 import PowerSet

class MyTestCase(unittest.TestCase):

    def test_put(self):
        '''тестируем put'''
        exemplar = PowerSet()
        val = '25'
        exemplar.put(val)
        result = exemplar.slots
        answer = {'25': '25'}
        self.assertEqual(result, answer)

        val = '25'
        exemplar.put(val)
        self.assertEqual(result, answer)

        val = '26'
        exemplar.put(val)
        result = exemplar.slots
        answer = {'25': '25', '26': '26'}
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
        result = exemplar.slots
        answer = {'25': '25'}
        self.assertEqual(result, answer)

        val = '27' # когда нет такого элемента
        exemplar.remove(val)
        self.assertEqual(result, answer)

        val = '25' # когда элемент последний
        exemplar.remove(val)
        result = exemplar.slots
        answer = {}
        self.assertEqual(result, answer)

    def test_intersection(self):
        '''тестируем intersection когда нет пересечений'''
        exemplar = PowerSet()
        for value in range(100, 20000):
            exemplar.put(str(value))
        exemplar2 = PowerSet()
        for value in range(50):
            exemplar2.put(str(value))
        set2 = exemplar2
        result = exemplar.intersection(exemplar2).slots
        answer = {}
        self.assertEqual(result, answer)

    def test_issubset(self):
        '''тестируем issubset подмножество'''
        exemplar = PowerSet()
        for value in range(10, 20000):
            exemplar.put(str(value))


        # все элементы параметра входят в текущее множество,
        exemplar2 = PowerSet()
        for value in range(10, 15):
            exemplar2.put(str(value))
        result = exemplar.issubset(exemplar2)
        answer = True
        self.assertEqual(result, answer)

        # не все элементы параметра входят в текущее множество,
        exemplar2 = PowerSet()
        for value in range(9, 15):
            exemplar2.put(str(value))
        result = exemplar.issubset(exemplar2)
        answer = False
        self.assertEqual(result, answer)

        # все элементы текущего множества входят в параметр,
        exemplar2 = PowerSet()
        for value in range(5, 20000):
            exemplar2.put(str(value))
        result = exemplar.issubset(exemplar2)
        answer = False
        self.assertEqual(result, answer)

    def test_union(self):
        '''тестируем union'''
        exemplar = PowerSet()
        for value in range(2, 5):
            exemplar.put(str(value))

        exemplar2 = PowerSet()
        for value in range(3, 10):
            exemplar2.put(str(value))

        result = exemplar.union(exemplar2).slots
        answer = {'2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}
        self.assertEqual(result, answer)

    def test_difference(self):
        '''тестируем difference'''
        exemplar = PowerSet()
        for value in range(2, 10):
            exemplar.put(str(value))

        exemplar2 = PowerSet()
        for value in range(5, 15):
            exemplar2.put(str(value))

        result = exemplar.difference(exemplar2).slots
        answer = {'2': '2', '3': '3', '4': '4', '10': '10', '11': '11', '12': '12', '13': '13', '14': '14'}
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
        '''тестируем size когда есть пересечение'''

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

    def test_intersection_(self):
        '''тестируем intersection'''
        exemplar = PowerSet()
        for value in range(2, 20000):
            exemplar.put(str(value))
        exemplar2 = PowerSet()
        for value in range(5, 10):
            exemplar2.put(str(value))
        set2 = exemplar2
        result = exemplar.intersection(exemplar2).slots
        answer = {'5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}
        self.assertEqual(result, answer)


if __name__ == '__main__':
    unittest.main()
