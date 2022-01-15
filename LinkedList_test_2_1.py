'''проверочные тесты'''

import unittest
from LinkedList2_1 import Node, LinkedList2

class TestCase_LinkedList2(unittest.TestCase):

    def test_clean(self):
        '''тестируем clean'''
        s_list = LinkedList2()
        s_list.add_in_tail(Node(10))
        s_list.add_in_tail(Node(20))
        s_list.add_in_tail(Node(30))
        s_list.clean()
        result_list = s_list.LinkedList_in_List()
        answer_list = []

        result_head = s_list.head
        result_tail = s_list.tail
        result_len = s_list.len()
        answer_head = None
        answer_tail = None
        answer_len = 0
        self.assertEqual(result_list, answer_list)
        self.assertEqual(result_head, answer_head)
        self.assertEqual(result_tail, answer_tail)
        self.assertEqual(result_len, answer_len)

    def test_add_in_head_empty(self):
        '''тестируем add_in_head в пустой список'''
        s_list = LinkedList2()
        s_list.add_in_head(Node(17))
        result_list = s_list.LinkedList_in_List()
        answer_list = [17]

        result_head_value = s_list.head.value
        result_head_prev = s_list.head.prev
        result_head_next = s_list.head.next
        result_tail_value = s_list.tail.value
        result_tail_prev = s_list.tail.prev
        result_tail_next = s_list.tail.next
        result_len = s_list.len()
        answer_head_value = 17
        answer_head_prev = None
        answer_head_next = None
        answer_tail_value = 17
        answer_tail_prev = None
        answer_tail_next = None
        answer_len = 1
        self.assertEqual(result_list, answer_list)
        self.assertEqual(result_head_value, answer_head_value)
        self.assertEqual(result_head_prev, answer_head_prev)
        self.assertEqual(result_head_next, answer_head_next)
        self.assertEqual(result_tail_value, answer_tail_value)
        self.assertEqual(result_tail_prev, answer_tail_prev)
        self.assertEqual(result_tail_next, answer_tail_next)
        self.assertEqual(result_len, answer_len)

    def test_add_in_head(self):
        '''тестируем add_in_head'''
        s_list = LinkedList2()
        s_list.add_in_tail(Node(10))
        s_list.add_in_tail(Node(20))
        s_list.add_in_tail(Node(30))
        s_list.add_in_head(Node(17))
        result_list = s_list.LinkedList_in_List()
        answer_list = [17, 10, 20, 30]

        result_head_value = s_list.head.value
        result_head_prev = s_list.head.prev
        result_head_next_value = s_list.head.next.value
        result_tail_value = s_list.tail.value
        result_tail_prev_value = s_list.tail.prev.value
        result_tail_next = s_list.tail.next
        result_len = s_list.len()
        answer_head_value = 17
        answer_head_prev = None
        answer_head_next_value = 10
        answer_tail_value = 30
        answer_tail_prev_value = 20
        answer_tail_next = None
        answer_len = 4
        self.assertEqual(result_list, answer_list)
        self.assertEqual(result_head_value, answer_head_value)
        self.assertEqual(result_head_prev, answer_head_prev)
        self.assertEqual(result_head_next_value, answer_head_next_value)
        self.assertEqual(result_tail_value, answer_tail_value)
        self.assertEqual(result_tail_prev_value, answer_tail_prev_value)
        self.assertEqual(result_tail_next, answer_tail_next)
        self.assertEqual(result_len, answer_len)

    def test_insert_tail(self):
        '''тестируем insert вставка в конец, в непустой список'''
        s_list = LinkedList2()
        s_list.add_in_tail(Node(10))
        s_list.add_in_tail(Node(20))
        s_list.add_in_tail(Node(30))
        s_list.insert(None, Node(17))
        result_list = s_list.LinkedList_in_List()
        answer_list = [10, 20, 30, 17]

        result_head_value = s_list.head.value
        result_head_prev = s_list.head.prev
        result_head_next_value = s_list.head.next.value
        result_tail_value = s_list.tail.value
        result_tail_prev_value = s_list.tail.prev.value
        result_tail_next = s_list.tail.next
        result_len = s_list.len()
        answer_head_value = 10
        answer_head_prev = None
        answer_head_next_value = 20
        answer_tail_value = 17
        answer_tail_prev_value = 30
        answer_tail_next = None
        answer_len = 4
        self.assertEqual(result_list, answer_list)
        self.assertEqual(result_head_value, answer_head_value)
        self.assertEqual(result_head_prev, answer_head_prev)
        self.assertEqual(result_head_next_value, answer_head_next_value)
        self.assertEqual(result_tail_value, answer_tail_value)
        self.assertEqual(result_tail_prev_value, answer_tail_prev_value)
        self.assertEqual(result_tail_next, answer_tail_next)
        self.assertEqual(result_len, answer_len)

    def test_insert_head(self):
        '''тестируем insert вставка в начало, в пустой список'''
        s_list = LinkedList2()
        s_list.insert(None, Node(17))
        result_list = s_list.LinkedList_in_List()
        answer_list = [17]

        result_head_value = s_list.head.value
        result_head_prev = s_list.head.prev
        # result_head_next_value = s_list.head.next.value
        result_tail_value = s_list.tail.value
        # result_tail_prev_value = s_list.tail.prev.value
        result_tail_next = s_list.tail.next
        result_len = s_list.len()
        answer_head_value = 17
        answer_head_prev = None
        # answer_head_next_value = 17
        answer_tail_value = 17
        # answer_tail_prev_value = 30
        answer_tail_next = None
        answer_len = 1
        self.assertEqual(result_list, answer_list)
        self.assertEqual(result_head_value, answer_head_value)
        self.assertEqual(result_head_prev, answer_head_prev)
        # self.assertEqual(result_head_next_value, answer_head_next_value)
        self.assertEqual(result_tail_value, answer_tail_value)
        # self.assertEqual(result_tail_prev_value, answer_tail_prev_value)
        self.assertEqual(result_tail_next, answer_tail_next)
        self.assertEqual(result_len, answer_len)

    def test_insert(self):
        '''тестируем insert вставка после определенного значения'''
        s_list = LinkedList2()
        s_list.add_in_tail(Node(10))
        s_list.add_in_tail(Node(20))
        s_list.add_in_tail(Node(30))
        s_list.add_in_tail(Node(25))
        s_list.insert(Node(10), Node(17))
        result_list = s_list.LinkedList_in_List()
        answer_list = [10, 17, 20, 30, 25]

        result_head_value = s_list.head.value
        result_head_prev = s_list.head.prev
        result_head_next_value = s_list.head.next.value
        result_tail_value = s_list.tail.value
        result_tail_prev_value = s_list.tail.prev.value
        result_tail_next = s_list.tail.next
        result_len = s_list.len()
        answer_head_value = 10
        answer_head_prev = None
        answer_head_next_value = 17
        answer_tail_value = 25
        answer_tail_prev_value = 30
        answer_tail_next = None
        answer_len = 5
        self.assertEqual(result_list, answer_list)
        self.assertEqual(result_head_value, answer_head_value)
        self.assertEqual(result_head_prev, answer_head_prev)
        self.assertEqual(result_head_next_value, answer_head_next_value)
        self.assertEqual(result_tail_value, answer_tail_value)
        self.assertEqual(result_tail_prev_value, answer_tail_prev_value)
        self.assertEqual(result_tail_next, answer_tail_next)
        self.assertEqual(result_len, answer_len)

    def test_delete_True(self):
        '''тестируем delete True совпадение в начале, в середине и в конце'''
        s_list = LinkedList2()
        s_list.add_in_tail(Node(10))
        s_list.add_in_tail(Node(10))
        s_list.add_in_tail(Node(20))
        s_list.add_in_tail(Node(10))
        s_list.add_in_tail(Node(10))
        s_list.add_in_tail(Node(15))
        s_list.add_in_tail(Node(10))
        s_list.add_in_tail(Node(30))
        s_list.add_in_tail(Node(25))
        s_list.add_in_tail(Node(10))
        s_list.add_in_tail(Node(10))
        s_list.delete(10, True)
        result_list = s_list.LinkedList_in_List()
        answer_list = [20, 15, 30, 25]

        result_head_value = s_list.head.value
        result_head_prev = s_list.head.prev
        result_head_next_value = s_list.head.next.value
        result_tail_value = s_list.tail.value
        result_tail_prev_value = s_list.tail.prev.value
        result_tail_next = s_list.tail.next
        result_len = s_list.len()
        answer_head_value = 20
        answer_head_prev = None
        answer_head_next_value = 15
        answer_tail_value = 25
        answer_tail_prev_value = 30
        answer_tail_next = None
        answer_len = 4
        self.assertEqual(result_list, answer_list)
        self.assertEqual(result_head_value, answer_head_value)
        self.assertEqual(result_head_prev, answer_head_prev)
        self.assertEqual(result_head_next_value, answer_head_next_value)
        self.assertEqual(result_tail_value, answer_tail_value)
        self.assertEqual(result_tail_prev_value, answer_tail_prev_value)
        self.assertEqual(result_tail_next, answer_tail_next)
        self.assertEqual(result_len, answer_len)

    def test_delete_True_tail(self):
        '''тестируем delete True совпадение только в конце'''
        s_list = LinkedList2()
        s_list.add_in_tail(Node(10))
        s_list.add_in_tail(Node(20))
        s_list.add_in_tail(Node(20))
        s_list.add_in_tail(Node(15))
        s_list.add_in_tail(Node(25))
        s_list.add_in_tail(Node(25))
        s_list.delete(25, True)
        result_list = s_list.LinkedList_in_List()
        answer_list = [10, 20, 20, 15]

        result_head_value = s_list.head.value
        result_head_prev = s_list.head.prev
        result_head_next_value = s_list.head.next.value
        result_tail_value = s_list.tail.value
        result_tail_prev_value = s_list.tail.prev.value
        result_tail_next = s_list.tail.next
        result_len = s_list.len()
        answer_head_value = 10
        answer_head_prev = None
        answer_head_next_value = 20
        answer_tail_value = 15
        answer_tail_prev_value = 20
        answer_tail_next = None
        answer_len = 4
        self.assertEqual(result_list, answer_list)
        self.assertEqual(result_head_value, answer_head_value)
        self.assertEqual(result_head_prev, answer_head_prev)
        self.assertEqual(result_head_next_value, answer_head_next_value)
        self.assertEqual(result_tail_value, answer_tail_value)
        self.assertEqual(result_tail_prev_value, answer_tail_prev_value)
        self.assertEqual(result_tail_next, answer_tail_next)
        self.assertEqual(result_len, answer_len)

    def test_delete_True_middle(self):
        '''тестируем delete True совпадение только в середине'''
        s_list = LinkedList2()
        s_list.add_in_tail(Node(10))
        s_list.add_in_tail(Node(20))
        s_list.add_in_tail(Node(20))
        s_list.add_in_tail(Node(15))
        s_list.add_in_tail(Node(30))
        s_list.delete(20, True)
        result_1 = s_list.LinkedList_in_List()
        answer_1 = [10, 15, 30]

        result_head_value = s_list.head.value
        result_head_prev = s_list.head.prev
        result_head_next_value = s_list.head.next.value
        result_tail_value = s_list.tail.value
        result_tail_prev_value = s_list.tail.prev.value
        result_tail_next = s_list.tail.next
        result_len = s_list.len()
        answer_head_value = 10
        answer_head_prev = None
        answer_head_next_value = 15
        answer_tail_value = 30
        answer_tail_prev_value = 15
        answer_tail_next = None
        answer_len = 3
        self.assertEqual(result_1, answer_1)
        self.assertEqual(result_head_value, answer_head_value)
        self.assertEqual(result_head_prev, answer_head_prev)
        self.assertEqual(result_head_next_value, answer_head_next_value)
        self.assertEqual(result_tail_value, answer_tail_value)
        self.assertEqual(result_tail_prev_value, answer_tail_prev_value)
        self.assertEqual(result_tail_next, answer_tail_next)
        self.assertEqual(result_len, answer_len)

    def test_delete_True_head(self):
        '''тестируем delete True совпадение только в начале'''
        s_list = LinkedList2()
        s_list.add_in_tail(Node(10))
        s_list.add_in_tail(Node(10))
        s_list.add_in_tail(Node(20))
        s_list.add_in_tail(Node(20))
        s_list.add_in_tail(Node(15))
        s_list.add_in_tail(Node(30))
        s_list.add_in_tail(Node(20))
        s_list.delete(10, True)
        result_1 = s_list.LinkedList_in_List()
        answer_1 = [20, 20, 15, 30, 20]

        result_head_value = s_list.head.value
        result_head_prev = s_list.head.prev
        result_head_next_value = s_list.head.next.value
        result_tail_value = s_list.tail.value
        result_tail_prev_value = s_list.tail.prev.value
        result_tail_next = s_list.tail.next
        result_len = s_list.len()
        answer_head_value = 20
        answer_head_prev = None
        answer_head_next_value = 20
        answer_tail_value = 20
        answer_tail_prev_value = 30
        answer_tail_next = None
        answer_len = 5
        self.assertEqual(result_1, answer_1)
        self.assertEqual(result_head_value, answer_head_value)
        self.assertEqual(result_head_prev, answer_head_prev)
        self.assertEqual(result_head_next_value, answer_head_next_value)
        self.assertEqual(result_tail_value, answer_tail_value)
        self.assertEqual(result_tail_prev_value, answer_tail_prev_value)
        self.assertEqual(result_tail_next, answer_tail_next)
        self.assertEqual(result_len, answer_len)

    def test_delete_False(self):
        '''тестируем delete False совпадение в начале'''
        s_list = LinkedList2()
        s_list.add_in_tail(Node(10))
        s_list.add_in_tail(Node(20))
        s_list.add_in_tail(Node(30))
        s_list.delete(10, False)
        result_1 = s_list.LinkedList_in_List()
        answer_1 = [20, 30]

        result_head_value = s_list.head.value
        result_head_prev = s_list.head.prev
        result_head_next_value = s_list.head.next.value
        result_tail_value = s_list.tail.value
        result_tail_prev_value = s_list.tail.prev.value
        result_tail_next = s_list.tail.next
        result_len = s_list.len()
        answer_head_value = 20
        answer_head_prev = None
        answer_head_next_value = 30
        answer_tail_value = 30
        answer_tail_prev_value = 20
        answer_tail_next = None
        answer_len = 2
        self.assertEqual(result_1, answer_1)
        self.assertEqual(result_head_value, answer_head_value)
        self.assertEqual(result_head_prev, answer_head_prev)
        self.assertEqual(result_head_next_value, answer_head_next_value)
        self.assertEqual(result_tail_value, answer_tail_value)
        self.assertEqual(result_tail_prev_value, answer_tail_prev_value)
        self.assertEqual(result_tail_next, answer_tail_next)
        self.assertEqual(result_len, answer_len)

    def test_delete_False(self):
        '''тестируем delete False совпадение в начале'''
        s_list = LinkedList2()
        s_list.add_in_tail(Node(10))
        s_list.add_in_tail(Node(20))
        s_list.add_in_tail(Node(30))
        s_list.delete(10, False)
        result_1 = s_list.LinkedList_in_List()
        answer_1 = [20, 30]

        result_head_value = s_list.head.value
        result_head_prev = s_list.head.prev
        result_head_next_value = s_list.head.next.value
        result_tail_value = s_list.tail.value
        result_tail_prev_value = s_list.tail.prev.value
        result_tail_next = s_list.tail.next
        result_len = s_list.len()
        answer_head_value = 20
        answer_head_prev = None
        answer_head_next_value = 30
        answer_tail_value = 30
        answer_tail_prev_value = 20
        answer_tail_next = None
        answer_len = 2
        self.assertEqual(result_1, answer_1)
        self.assertEqual(result_head_value, answer_head_value)
        self.assertEqual(result_head_prev, answer_head_prev)
        self.assertEqual(result_head_next_value, answer_head_next_value)
        self.assertEqual(result_tail_value, answer_tail_value)
        self.assertEqual(result_tail_prev_value, answer_tail_prev_value)
        self.assertEqual(result_tail_next, answer_tail_next)
        self.assertEqual(result_len, answer_len)

    def test_find(self):
        '''тестируем find'''
        s_list = LinkedList2()
        s_list.add_in_tail(Node(10))
        s_list.add_in_tail(Node(20))
        s_list.add_in_tail(Node(30))
        nf = s_list.find(20)
        result_1 = nf.value
        answer_1 = 20
        self.assertEqual(result_1, answer_1)

    def test_add_in_tail(self):
        '''тестируем добавление узлов, смотрим параметры списка'''
        s_list = LinkedList2()
        s_list.add_in_tail(Node(10))
        s_list.add_in_tail(Node(20))
        s_list.add_in_tail(Node(30))
        result_1 = s_list.LinkedList_in_List()
        answer_1 = [10, 20, 30]

        result_11 = s_list.head.value
        result_2 = s_list.head.prev
        result_3 = s_list.head.next.value
        result_4 = s_list.tail.value
        result_5 = s_list.tail.prev.value
        result_6 = s_list.tail.next
        result_7 = s_list.len()
        answer_11 = 10
        answer_2 = None
        answer_3 = 20
        answer_4 = 30
        answer_5 = 20
        answer_6 = None
        answer_7 = 3
        self.assertEqual(result_1, answer_1)
        self.assertEqual(result_11, answer_11)
        self.assertEqual(result_2, answer_2)
        self.assertEqual(result_3, answer_3)
        self.assertEqual(result_4, answer_4)
        self.assertEqual(result_5, answer_5)
        self.assertEqual(result_6, answer_6)
        self.assertEqual(result_7, answer_7)
