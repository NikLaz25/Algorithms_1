'''
2. Переделайте реализацию стека так, чтобы она работала не с хвостом списка
как с верхушкой стека, а с его головой.
'''

from typing import Optional
from typing import Any
from typing import Union


class Stack:
    '''класс Стек'''

    def __init__(self):
        '''Конструктор'''
        self.stack = []

    def size(self) -> int:
        '''размер стека'''
        return len(self.stack)

    def pop(self) -> Union[int, str]: #мера сложности О(n)
        '''вернуть'''
        if len(self.stack) > 0: #мера сложности О(n)
            target = self.stack[0]
            self.stack = self.stack[1:]
            return target
        else:
            return None # если стек пустой

    def push(self, value: Union[int, str, float]) -> Optional[list]:  # мера сложности О(n)
        '''вставить'''
        stack_insert = self.stack[::-1]  # мера сложности О(n)
        stack_insert += [value]  # мера сложности О(1)
        self.stack = stack_insert[::-1]  # мера сложности О(n)
        return self.stack

    def peek(self) -> Any:  # мера сложности О(n)
        '''получить верхний элемент стека, но не удалять его'''
        if len(self.stack) > 0:  # мера сложности О(n)
            return self.stack[0]  # мера сложности О(1)
        else:
            return None  # если стек пустой

# stack = Stack()
# stack.push('*')
# stack.push(3)
#
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())


# def balance(my_str: str) -> bool:
#     stack = Stack()
#     count = 0
#     for i in range(len(my_str)):
#         stack.push(my_str[i])
#     for i in range(len(stack.stack)):
#         if  stack.peek() == ')':
#             count += 1
#         elif  stack.peek() == '(':
#             count -= 1
#         stack.pop()
#     if count == 0:
#         return True
#     else:
#         return False
#
# my_str = '(())'
# print(balance(my_str))