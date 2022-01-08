class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item 
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.head
        find_list = []
        while node is not None:
            if node.value == val:
                #                 find_list += [node.value]
                find_list += [node]
            node = node.next
        return find_list # здесь будет ваш код

    def delete(self, val, all=False):
        node = self.head
        if node == None: #Отрабатывает пустой список
            return
        if all == False:
            while node is not None:
                if self.head.value == val: #Когда удаляем первое число
                    self.head = node.next
                    return
                elif node.value == val and node.next is not None: # Удаляем число в середине
                    last_node.next = node.next
                    return
                elif node.value == val and node.next is None: # Удаляем число в конце
                    last_node.next = None
                    self.tail = last_node
                else: #Ничего не происходит
                    last_node = node
                node = node.next
            return
        else:
            while node is not None:
                if self.head.value == val:
                    self.head = node.next
                elif node.value == val and node.next is not None: # Удаляем число в середине
                    last_node.next = node.next
                elif node.value == val and node.next is None: # Удаляем число в конце
                    last_node.next = None
                    self.tail = last_node
                else:
                    last_node = node
                node = node.next
            return

    def clean(self):
        self.head = None
        return

    def len(self):
        node = self.head
        counter = 0
        while node is not None:
            counter += 1
            node = node.next
        return counter # здесь будет ваш код

    def insert(self, afterNode, newNode):
        node = self.head
        new_node = Node(newNode)
        if afterNode is not None:
            while node is not None:
                last_node = node
                node = node.next
                if last_node.value == afterNode and last_node.value != self.tail.value:
                    new_node.next = last_node.next
                    last_node.next = new_node
                    return
                elif last_node.value == afterNode and last_node.value == self.tail.value:
                    new_node.next = last_node.next
                    last_node.next = new_node
                    self.tail = new_node
                    return
        else:
            second_node = self.head
            self.head = new_node
            node = new_node
            node.next = second_node
        return

    def LinkedList_in_List(self):
        node = self.head
        my_list = []
        while node is not None:
            my_list += [node.value]
            node = node.next
        return my_list
# s_list = LinkedList()
# s_list.add_in_tail(Node(125))
# # s_list.add_in_tail(Node(128))
# s_list.print_all_nodes()
# x = s_list.Summa_2(2, 3)
#

# s_list = LinkedList()
# n1 = Node(12)
# n2 = Node(55)
# n1.next = n2
# s_list.add_in_tail(n1)
# s_list.add_in_tail(Node(12))
# s_list.add_in_tail(Node(128))
# s_list.add_in_tail(n2)
# s_list.add_in_tail(Node(125))
# s_list.add_in_tail(Node(128))
# # s_list.delete(12, False)
# s_list.print_all_nodes()
# print(s_list.find_all(128))
# # print(s_list.LinkedList_in_List())