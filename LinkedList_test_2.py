'''проверочные тесты'''

import unittest
from LinkedList_4 import Node, LinkedList

class TestCase_1(unittest.TestCase):

    def test_insert_None(self):
        '''тестируем insert_None вставка значения в пустой список'''
        s_list = LinkedList()

        s_list.insert(None, 5)
        result = s_list.LinkedList_in_List()
        answer = [5]
        self.assertEqual(result, answer)




if __name__ == '__main__':
    unittest.main()