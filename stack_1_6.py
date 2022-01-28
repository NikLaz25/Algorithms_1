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

    def pop(self) -> Optional[Union[int, str]]: #мера сложности О(n)
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

def postfix_calculation(stack_1, stack_2) -> Union[int, float]:
    '''функция вычисления постфиксных выражений'''
    while len(stack_1.stack) > 0:
#         print('stack_2: ', stack_2.stack)
        item = stack_1.pop()
        if type(item) is int:
            stack_2.push(item)
        elif item == '*':
            stack_2.push(stack_2.pop() * stack_2.pop())
        elif item == '+':
            stack_2.push(stack_2.pop() + stack_2.pop())
        elif item == '-':
            item_2 = stack_2.pop()
            item_1 = stack_2.pop()
            stack_2.push(item_1 - item_2)
#             print('- вычисление: ',stack_2.peek())

        elif item == '/':
            item_2 = stack_2.pop()
            item_1 = stack_2.pop()
            try:
                stack_2.push(item_1 / item_2)
            except:
#                 print('Деление на ноль')
                pass
    return stack_2.peek()


# # задание 6 деление
# # формируем стек_1 = 1 2 - 3 /
# stack_1 = Stack()
# stack_1.push('/')
# stack_1.push(3)
# stack_1.push('-')
# stack_1.push(2)
# stack_1.push(1)
# # print(stack_1.stack)
#
# # формируем пустой стек_2
# stack_2 = Stack()
# stack_2.stack
# print(postfix_calculation(stack_1, stack_2))