import unittest
from stack_1_1 import Stack

class MyTestCase(unittest.TestCase):
    def test_size(self):
        '''Тестируем push, size and stack, peek'''
        stack = Stack()
        stack.push(5)
        stack.push(6)
        stack.push(7)
        stack.push(1)
        stack.push(1)
        stack.push("2")
        stack.push(3.14)
        result_size = stack.size()
        answer_size = 7
        self.assertEqual(result_size, answer_size)
        result_stack = stack.stack
        answer_stack = [5, 6, 7, 1, 1, '2', 3.14]
        self.assertEqual(result_stack, answer_stack)
        result_peek = stack.peek()
        answer_peek = 3.14
        self.assertEqual(result_peek, answer_peek)
        result_pop = stack.pop()
        answer_pop = [5, 6, 7, 1, 1, '2']
        self.assertEqual(result_pop, answer_pop)


if __name__ == '__main__':
    unittest.main()