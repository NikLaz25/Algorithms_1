class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key # ключ узла
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок


class BSTFind: # промежуточный результат поиска

    def __init__(self):
        self.Node = None # None если 
        # в дереве вообще нету узлов

        self.NodeHasKey = False # True если узел найден
        self.ToLeft = False # True, если родительскому узлу надо добавить новый узел левым потомком


class BST:

    def __init__(self, node):
        self.Root = node # корень дерева, или None

        
    def FindByKey_node(self, key, node):
        if key == node.NodeKey:
            return [node, True, False]
        if node.LeftChild is not None and key < node.NodeKey:
            return self.FindByKey_node(key, node.LeftChild)

        elif node.RightChild is not None and key > node.NodeKey:
            return self.FindByKey_node(key, node.RightChild)
        
        elif node.LeftChild is None and key < node.NodeKey:
            return [node, False, True]
        elif node.RightChild is None and key > node.NodeKey:
            return [node, False, False]


    def FindNodeByKey(self, key):
        # ищем в дереве узел и сопутствующую информацию по ключу
        # return None # возвращает BSTFind
        
        find_node = self.FindByKey_node(key, self.Root)
        BSTF_ekz = BSTFind()
        
        BSTF_ekz.Node = find_node[0]
        BSTF_ekz.NodeHasKey = find_node[1]
        BSTF_ekz.ToLeft = find_node[2]

        find_node_list = []
        find_node_list.append(BSTF_ekz.Node)
        find_node_list.append(BSTF_ekz.NodeHasKey)
        find_node_list.append(BSTF_ekz.ToLeft)
        return find_node_list

    def init_new_node(self, new_key, new_val, new_parent, ToLeft):
        new_node = BSTNode(new_key, new_val, new_parent)
        if ToLeft == True:
            new_parent.LeftChild = new_node
        else:
            new_parent.RightChild = new_node
        
    
    def AddKeyValue(self, key, val):
        # добавляем ключ-значение в дерево
        find_node_list = self.FindNodeByKey(key)
        if find_node_list[1] == False:
            self.init_new_node(key, val, find_node_list[0], find_node_list[2])
            
        if find_node_list[1] == True:         
            return False # если ключ уже есть
  
    def FinMinMax(self, FromNode, FindMax):
        # ищем максимальный/минимальный ключ в поддереве
        # возвращается объект типа BSTNode
        if FindMax is True and FromNode.RightChild is not None:
            return self.FinMinMax(FromNode.RightChild, FindMax)
        elif FindMax is True and FromNode.RightChild is None:
            return FromNode

        elif FindMax == False and FromNode.LeftChild is not None:
            return self.FinMinMax(FromNode.LeftChild, FindMax)
        elif FindMax == False and FromNode.LeftChild is None:
            return FromNode

    def DeleteNodeByKey(self, key):
        # удаляем узел по ключу
        delet_node = self.FindNodeByKey(key)
        if delet_node[1] == True:
            delet_node = delet_node[0]

            if delet_node.RightChild is not None:
                new_node = self.FinMinMax(delet_node.RightChild, False)          
            
            if delet_node.Parent is None:
                self.Root = new_node
            elif delet_node.NodeKey < delet_node.Parent.NodeKey:
                delet_node.Parent.LeftChild = new_node
            elif delet_node.NodeKey > delet_node.Parent.NodeKey:
                delet_node.Parent.RightChild = new_node
                
            new_node.LeftChild = delet_node.LeftChild
            new_node.Parent = delet_node.Parent

        else:
            return False # если узел не найден

    def counter(self, node, count_number):
        count_number += 1
        if node.LeftChild is not None:
            count_number = self.counter(node.LeftChild, count_number)
        if node.RightChild is not None:
            count_number = self.counter(node.RightChild, count_number)
        return count_number
        
    def Count(self):
        return self.counter(self.Root, 0) # количество узлов в дереве
    
    def print_tree_key(self, node):
        print('Узел')
        print('NodeKey', node.NodeKey)
        if node.Parent is not None:
            print('Parent_key', node.Parent.NodeKey)
        else:
            print('Parent', node.Parent)
        if node.LeftChild is not None:
            print('LeftChild_Key', node.LeftChild.NodeKey)
        else:
            print('LeftChild', node.LeftChild)
        if node.RightChild is not None:
            print('RightChild_Key', node.RightChild.NodeKey)
        else:
            print('RightChild', node.RightChild)
        print('')
        if node.LeftChild is not None:
            self.print_tree_key(node.LeftChild)
        if node.RightChild is not None:
            self.print_tree_key(node.RightChild)
    def ezy_print_tree_key(self, node):
        print(node.NodeKey)

        if node.LeftChild is not None:
            self.ezy_print_tree_key(node.LeftChild)
        if node.RightChild is not None:
            self.ezy_print_tree_key(node.RightChild)
