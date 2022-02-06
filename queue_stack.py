'''
Осваиваю очередь на основе двух стеков
'''

# Задание 1
''' методы size(), pop(), push() и peek().
Добавьте тесты для каждого из этих четырёх методов.
Оцените меру сложности для операций pop и push.'''

import ctypes
from typing import Optional
from typing import Any
from typing import Union


class Stack:
    '''класс Стек'''

    def __init__(self):
        '''Конструктор'''
        self.stack = []
        self.stack_2 = []

    def size(self) -> int:  # мера сложности О(n)
        '''размер стека'''
        return len(self.stack)

    def pop(self) -> Optional[Union[int, str]]:  # мера сложности О(n)
        '''вернуть'''
        if len(self.stack) > 0:  # мера сложности О(n)
            target = self.stack[-1]
            self.stack = self.stack[: -1]
            return target
        else:
            return None  # если стек пустой

    def push(self, value: int) -> Optional[list]:  # мера сложности О(1)
        '''вставить'''
        self.stack += [value]
        return self.stack

    def peek(self) -> Any:  # мера сложности О(n)
        '''получить верхний элемент стека, но не удалять его'''
        if len(self.stack) > 0:  # мера сложности О(n)
            return self.stack[len(self.stack) - 1]  # мера сложности О(n)
        else:
            return None  # если стек пустой

stack_1 = Stack()

stack_1.push(3)
stack_1.push(2)
stack_1.push(1)
print('stack_1: ', stack_1.stack)

stack_2 = Stack()
print('stack_2: ', stack_2.stack)


def dequeue(stack_1, stack_2):
    '''выдача из головы на основании использования двух стеков'''
    len_stack = len(stack_1.stack)
    if len_stack == 0:
        return None

    count = 0
    while count < (len_stack - 1):
        stack_2.push(stack_1.pop())
        count += 1

    target = stack_1.pop()

    while count > 0:
        stack_1.push(stack_2.pop())
        count -= 1
    return target

print(dequeue(stack_1, stack_2))
