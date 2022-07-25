class SimpleTreeNode:
    def __init__(self, val, parent):
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.Children = [] # список дочерних узлов

class SimpleTree:

    def __init__(self, root):
        self.Root = root # корень, может быть None

    def AddChild(self, ParentNode, NewChild):
        '''добавление нового дочернего узла существующему ParentNode'''
        if self.Root is None:
            self.Root = NewChild
        else:
            node = NewChild
            node.Parent = ParentNode
            ParentNode.Children.append(NewChild)
            
    def DeleteNode(self, NodeToDelete):
        '''удаление существующего узла NodeToDelete'''
        NodeToDelete.Parent.Children.remove(NodeToDelete)
        NodeToDelete.Parent = None

    def GetAllNodes(self):
        '''выдача всех узлов дерева в определённом порядке'''
        node = self.Root
        get_all_nodes_list = self.GetAllNodes_recurtion(node)
        return get_all_nodes_list
    
    def GetAllNodes_recurtion(self, node):
        '''выдача всех узлов дерева в определённом порядке'''
        get_all_nodes_list = []
        get_all_nodes_list.append(node)
        if len(node.Children) > 0:
            for i in node.Children:
                get_all_nodes_list += self.GetAllNodes_recurtion(i)          
        return get_all_nodes_list
   
    def FindNodesByValue(self, val):
        '''поиск узлов по значению'''
        node = self.Root
        find_value_list = []
        get_all_nodes_list = self.GetAllNodes_recurtion(node)
        for i in get_all_nodes_list:
            if i.NodeValue == val:
                find_value_list.append(i)    
        return find_value_list
    
    def MoveNode(self, OriginalNode, NewParent):
        '''ваш код перемещения узла вместе с его поддеревом в качестве дочернего для узла NewParent'''
        # У старого родителя список должет уменьшится
        OriginalNode.Parent.Children.remove(OriginalNode)
        # у нового родителя список должет пополнится
        NewParent.Children.append(OriginalNode)
        # у нода должен поменяться родитель
        OriginalNode.Parent = NewParent
      
    def Count(self):
        '''количество всех узлов в дереве'''
        return len(self.GetAllNodes())

    def LeafCount(self):
        '''количество листьев в дереве'''
        get_all_nodes = self.GetAllNodes()
        quantity_of_leaves = 0
        
        for i in get_all_nodes:
            if len(i.Children) == 0:
                quantity_of_leaves += 1
        return quantity_of_leaves
    
    def print_elements(self, node):
        '''вспомогательный метод, печать всех значений узлов дерева'''
        print(node.NodeValue)
        if len(node.Children) > 0:
            for i in node.Children:
                self.print_elements(i)