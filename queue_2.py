'''
Осваиваю двойную очередь на основе стандартного списка
'''

class Deque:
    def __init__(self):
        '''инициализация внутреннего хранилища'''
        self.my_list = []

    def addFront(self, item):
        '''добавление в голову'''
        self.my_list = [item] + self.my_list
        return self.my_list

    def addTail(self, item):
        '''добавление в хвост'''
        self.my_list = self.my_list + [item]
        return self.my_list

    def removeFront(self):
        '''удаление из головы'''
        if len(self.my_list) == 0:  # если очередь пустая
            return None
        result = self.my_list[0]
        del self.my_list[0]
        return result

    def removeTail(self):
        '''удаление из хвоста'''
        if len(self.my_list) == 0:  # если очередь пустая
            return None
        result = self.my_list[-1]
        del self.my_list[-1]
        return result

    def size(self):
        '''размер очереди'''
        return len(self.my_list)  # размер очереди

    def print_list(self):
        return self.my_list


# def check_polinom(polinom):
#     deq = Deque()
#     for i in polinom:
#         deq.addTail(i)
#     while len(deq.my_list) > 0:
#         item_Front = deq.removeFront()
#         item_Tail = deq.removeTail()
#         if item_Front == item_Tail or item_Tail is None:
#             pass
#         else:
#             return False
#
#     return True
#
# polinom = 'my123_321ym'
#
# print(check_polinom(polinom))
