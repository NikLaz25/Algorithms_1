import unittest
from OrderedList_1 import Node, OrderedList, OrderedStringList

class MyTestCase(unittest.TestCase):
    def test_add(self):
        '''тестируем add asc = True'''
        asc = True
        new_object = OrderedList(asc)
        new_object.add(3)
        new_object.add(1)
        new_object.add(2)
        new_object.add(0)
        new_object.add(4)
        result = new_object.LinkedList_in_List()
        answer = [0, 1, 2, 3, 4]
        self.assertEqual(result, answer)

        '''тестируем add asc = False'''
        asc = False
        new_object = OrderedList(asc)
        new_object.add(3)
        new_object.add(1)
        new_object.add(2)
        new_object.add(4)
        new_object.add(0)
        result = new_object.LinkedList_in_List()
        answer = [4, 3, 2, 1, 0]
        self.assertEqual(result, answer)

    def test_find(self):
        '''тестируем find'''
        asc = True
        new_object = OrderedList(asc)
        new_object.add(3)
        new_object.add(1)
        new_object.add(2)
        result = new_object.find(3).value
        answer = 3
        self.assertEqual(result, answer)

        result = new_object.find(1).value
        answer = 1
        self.assertEqual(result, answer)

        result = new_object.find(2).value
        answer = 2
        self.assertEqual(result, answer)

    def test_clean(self):
        '''тестируем clean'''
        asc = True
        new_object = OrderedList(asc)
        new_object.add(3)
        new_object.add(1)
        new_object.add(2)
        new_object.clean(asc)
        result = new_object.LinkedList_in_List()
        answer = []
        self.assertEqual(result, answer)

    def test_len(self):
        '''тестируем len'''
        asc = True
        new_object = OrderedList(asc)
        new_object.add(3)
        new_object.add(1)
        new_object.add(2)
        result = new_object.len()
        answer = 3
        self.assertEqual(result, answer)

    def test_get_all(self):
        '''тестируем get_all'''
        asc = True
        new_object = OrderedList(asc)
        new_object.add(3)
        new_object.add(1)
        new_object.add(2)
        result = len(new_object.get_all())
        answer = 3
        self.assertEqual(result, answer)

    def test_OrderedStringList(self):
        '''тестируем OrderedStringList'''
        asc = True
        new_object = OrderedStringList(asc)
        result = new_object.compare('qwe', ' ww ')
        answer = 1
        self.assertEqual(result, answer)
        result = new_object.compare('qwe', ' wwe ')
        answer = 0
        self.assertEqual(result, answer)
        result = new_object.compare('qwe', ' wwew ')
        answer = -1
        self.assertEqual(result, answer)

    def test_delete_true(self):
        '''тестируем delete asc = True '''
        asc = True
        new_object = OrderedList(asc)
        new_object.add(2)
        new_object.add(5)
        new_object.add(7)
        new_object.add(9)
        new_object.add(0)
        new_object.delete(7)
        result = new_object.LinkedList_in_List()
        answer = [0, 2, 5, 9]
        self.assertEqual(result, answer)

        new_object.delete(2)
        result = new_object.LinkedList_in_List()
        answer = [0, 5, 9]
        self.assertEqual(result, answer)

        new_object.delete(5)
        result = new_object.LinkedList_in_List()
        answer = [0, 9]
        self.assertEqual(result, answer)

        new_object.delete(0)
        result = new_object.LinkedList_in_List()
        answer = [9]
        self.assertEqual(result, answer)

        new_object.delete(9)
        result = new_object.LinkedList_in_List()
        answer = []
        self.assertEqual(result, answer)

    def test_delete_false(self):
        '''тестируем delete asc = True '''
        asc = False
        new_object = OrderedList(asc)
        new_object.add(2)
        new_object.add(5)
        new_object.add(7)
        new_object.add(9)
        new_object.add(0)
        new_object.delete(7)
        result = new_object.LinkedList_in_List()
        answer = [9, 5, 2, 0]
        self.assertEqual(result, answer)

        new_object.delete(2)
        result = new_object.LinkedList_in_List()
        answer = [9, 5, 0]
        self.assertEqual(result, answer)

        new_object.delete(5)
        result = new_object.LinkedList_in_List()
        answer = [9, 0]
        self.assertEqual(result, answer)

        new_object.delete(0)
        result = new_object.LinkedList_in_List()
        answer = [9]
        self.assertEqual(result, answer)

        new_object.delete(9)
        result = new_object.LinkedList_in_List()
        answer = []
        self.assertEqual(result, answer)

if __name__ == '__main__':
    unittest.main()
