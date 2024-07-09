# creating the binary search tree

import QueueLinkedList

class BSTNode:
    def __init__(self,data):
        self.data = data
        self.left_child = None
        self.right_child = None

#Inserting a node
def InsertNode(rootNode,nodeValue):
    if rootNode.data ==None:
        rootNode.data = nodeValue
    elif rootNode.data>=nodeValue:
        if rootNode.left_child == None:
            rootNode.left_child = BSTNode(nodeValue)
        else:InsertNode(rootNode.left_child,nodeValue)
    else:
        if rootNode.right_child == None:
            rootNode.right_child = BSTNode(nodeValue)
        else:InsertNode(rootNode.right_child,nodeValue)
    return "The node is successfully added"

def PreOrderTraverse(rootNode):
    if rootNode is None:
        return
    print(rootNode.data)
    PreOrderTraverse(rootNode.left_child)
    PreOrderTraverse(rootNode.right_child)

def InoederTraverse(rootNode):
    if rootNode is None:
        return
    InoederTraverse(rootNode.left_child)
    print(rootNode.data)
    InoederTraverse(rootNode.right_child)
#preorder and postorder are the same thing only the place of printing changes

def postOrderTraverse(rootNode):
    if rootNode is None:
        return
    postOrderTraverse(rootNode.left_child)
    postOrderTraverse(rootNode.right_child)
    print(rootNode.data)


def levelOrderTraverse(rootNode):    
    if rootNode is None:
        return
    else:
        bst_queue = QueueLinkedList.Queue()
        bst_queue.Enqueue(rootNode)
        while not (bst_queue.isEmpty()):
            root = bst_queue.Dequeue()
            print(root.value.data)
            if(root.value.left_child is not None):
                bst_queue.Enqueue(root.value.left_child)
            if(root.value.right_child is not None):
                bst_queue.Enqueue(root.value.right_child)
                
def BinarySearch(rootNode, value):
    if rootNode is None or rootNode.data is None:
        print("Tree is empty")
        return
    while rootNode is not None:
        if rootNode.data == value:
            print("Value found in the tree")
            return
        elif rootNode.data > value:
            rootNode = rootNode.left_child
        else:
            rootNode = rootNode.right_child
    print("Value not found in the tree")
    
# for deleting a node we need to find the minimum value of a tree(incase where there are two childs for the node we are deleting we need the smallest value of the tree with node of that parent0
# )
def minValue(bstNode):
    current = bstNode
    while current.left_child is not None:# at the most left corner of a tree has the lowest value
        current = current.left_child
    return current

def deleteBSTNode(rootNode,value):
    pass # need to complete this
                    
    
    
# successor : smallest node in the right subtree 
#########################################################################################################################
         
newBst = BSTNode(None)
print(InsertNode(newBst,70))
print(InsertNode(newBst,40))
print(InsertNode(newBst,50))
print(InsertNode(newBst,100))
print(InsertNode(newBst,10))
print(InsertNode(newBst,90))


InoederTraverse(newBst)


        