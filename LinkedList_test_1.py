'''проверочные тесты'''

import unittest
from LinkedList_3 import Node, LinkedList

class TestCase_1(unittest.TestCase):
    '''Тестирование'''
    # def __init__(self):
    #     self.s_list = LinkedList()
    #     # self.node1 = Node(1)
    '''Тестирование для случая, когда список содержит несколько или много элементов'''
    def test_print_all_nodes(self):
        '''тестируем add_in_tail 1 значение'''
        s_list = LinkedList()
        s_list.add_in_tail(Node(125))
        result = s_list.LinkedList_in_List()
        answer = [125]
        self.assertEqual(result, answer)
    def test_print_all_nodes(self):
        '''тестируем add_in_tail 2 значения'''
        s_list = LinkedList()
        s_list.clean()
        s_list.add_in_tail(Node(125))
        s_list.add_in_tail(Node(128))
        result = s_list.LinkedList_in_List()
        answer = [125, 128]
        self.assertEqual(result, answer)
    def test_delete(self):
        '''тестируем delete 1 значение all=False'''
        s_list = LinkedList()
        n1 = Node(12)
        n2 = Node(55)
        n1.next = n2
        s_list.add_in_tail(n1)
        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(13))
        s_list.add_in_tail(n2)
        s_list.add_in_tail(Node(125))
        s_list.add_in_tail(Node(128))
        s_list.delete(12, False)
        result = s_list.LinkedList_in_List()
        answer = [12, 13, 55, 125, 128]
        self.assertEqual(result, answer)
    def test_delete(self):
        '''тестируем delete 1 значение all=True'''
        s_list = LinkedList()
        n1 = Node(12)
        n2 = Node(55)
        n1.next = n2
        s_list.add_in_tail(n1)
        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(13))
        s_list.add_in_tail(n2)
        s_list.add_in_tail(Node(125))
        s_list.add_in_tail(Node(128))
        s_list.add_in_tail(Node(12))
        s_list.delete(12, True)
        result = s_list.LinkedList_in_List()
        answer = [13, 55, 125, 128]
        self.assertEqual(result, answer)
    def test_clean(self):
        '''тестируем clean'''
        s_list = LinkedList()
        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(13))
        s_list.clean()
        result = s_list.LinkedList_in_List()
        answer = []
        self.assertEqual(result, answer)

    def test_insert(self):
        '''тестируем insert'''
        s_list = LinkedList()
        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(13))
        s_list.add_in_tail(Node(125))
        s_list.add_in_tail(Node(128))
        s_list.add_in_tail(Node(12))
        s_list.insert(125, 5)
        result = s_list.LinkedList_in_List()
        answer = [12, 13, 125, 5, 128, 12]
        self.assertEqual(result, answer)
    def test_insert_None(self):
        '''тестируем insert_None'''
        s_list = LinkedList()
        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(13))
        s_list.insert(None, 5)
        result = s_list.LinkedList_in_List()
        answer = [5, 12, 13]
        self.assertEqual(result, answer)

    '''Тестирование для случая, когда список пустой'''
    def test_print_all_nodes(self):
        '''тестируем add_in_tail 1 значение'''
        s_list = LinkedList()
        s_list.add_in_tail(Node(None))
        result = s_list.LinkedList_in_List()
        answer = [None]
        self.assertEqual(result, answer)
    def test_delete(self):
        '''тестируем delete 1 значение all=False'''
        s_list = LinkedList()
        s_list.delete(12, False)
        result = s_list.LinkedList_in_List()
        answer = []
        self.assertEqual(result, answer)
    def test_delete(self):
        '''тестируем delete 1 значение all=True'''
        s_list = LinkedList()
        s_list.delete(12, True)
        result = s_list.LinkedList_in_List()
        answer = []
        self.assertEqual(result, answer)
    def test_clean(self):
        '''тестируем clean'''
        s_list = LinkedList()
        s_list.clean()
        result = s_list.LinkedList_in_List()
        answer = []
        self.assertEqual(result, answer)
    # def test_find_all(self):
    #     '''тестируем find_all'''
    #     s_list = LinkedList()
    #     result = s_list.find_all(12)
    #     answer = []
    #     self.assertEqual(result, answer)
    def test_insert(self):
        '''тестируем insert'''
        s_list = LinkedList()
        s_list.insert(125, 5)
        result = s_list.LinkedList_in_List()
        answer = []
        self.assertEqual(result, answer)
    def test_insert_None(self):
        '''тестируем insert_None'''
        s_list = LinkedList()
        s_list.insert(None, 5)
        result = s_list.LinkedList_in_List()
        answer = [5]
        self.assertEqual(result, answer)
    '''Тестирование для случая, когда список содержит один элемент'''

    def test_delete(self):
        '''тестируем delete 1 значение all=False'''
        s_list = LinkedList()
        s_list.add_in_tail(Node(12))

        s_list.delete(12, False)
        result = s_list.LinkedList_in_List()
        answer = []
        self.assertEqual(result, answer)

    def test_delete(self):
        '''тестируем delete 1 значение all=True'''
        s_list = LinkedList()
        s_list.add_in_tail(Node(12))
        s_list.delete(12, True)
        result = s_list.LinkedList_in_List()
        answer = []
        self.assertEqual(result, answer)

    def test_clean(self):
        '''тестируем clean'''
        s_list = LinkedList()
        s_list.add_in_tail(Node(12))
        s_list.clean()
        result = s_list.LinkedList_in_List()
        answer = []
        self.assertEqual(result, answer)


    def test_insert(self):
        '''тестируем insert'''
        s_list = LinkedList()
        s_list.add_in_tail(Node(12))

        s_list.insert(12, 5)
        result = s_list.LinkedList_in_List()
        answer = [12, 5]
        self.assertEqual(result, answer)

    def test_insert_None(self):
        '''тестируем insert_None'''
        s_list = LinkedList()
        s_list.add_in_tail(Node(12))

        s_list.insert(None, 5)
        result = s_list.LinkedList_in_List()
        answer = [5, 12]
        self.assertEqual(result, answer)

    def test_insert_None(self):
        '''тестируем insert_None вставка значения в пустой список'''
        s_list = LinkedList()

        s_list.insert(None, 5)
        result = s_list.LinkedList_in_List()
        answer = [5]
        self.assertEqual(result, answer)
if __name__ == '__main__':
    unittest.main()

