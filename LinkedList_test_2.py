'''проверочные тесты'''

import unittest
from LinkedList_4 import Node, LinkedList

class TestCase_1(unittest.TestCase):

    def test_insert_None(self):
        '''тестируем insert_None вставка значения в пустой список'''
        s_list = LinkedList()

        s_list.insert(None, 15)
        result_1 = s_list.LinkedList_in_List()
        answer_1 = [15]
        result_2 = s_list.head.value
        answer_2 = 15
        result_3 = s_list.tail.value
        answer_3 = 15
        result_4 = s_list.tail.next
        answer_4 = None
        self.assertEqual(result_1, answer_1)
        self.assertEqual(result_2, answer_2)
        self.assertEqual(result_3, answer_3)
        self.assertEqual(result_4, answer_4)




if __name__ == '__main__':
    unittest.main()