class AVLNode:
    def __init__(self,data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
        self.height = 1


def preorderTraverse(avlrootNode):
    if avlrootNode is None:
        return
    else:
        print(avlrootNode.data)
        preorderTraverse(avlrootNode.leftchild)
        preorderTraverse(avlrootNode.rightchild)
        
def inordertraverse(avlrootNode):
    if avlrootNode is None:
        return
    else:
        inordertraverse(avlrootNode.leftchild)
        print(avlrootNode.data)
        inordertraverse(avlrootNode.rightchild)
        
def postorderTraverse(avlrootNode):
    if avlrootNode is None:
        return
    else:
        postorderTraverse(avlrootNode.leftchild)
        postorderTraverse(avlrootNode.rightchild)
        print(avlrootNode.data)
        
def searchNodeinAVL(rootNode, value):
    if rootNode is None or rootNode.data is None:
        print("The value is not found")
        return 
    else:
        while rootNode is not None:
            if rootNode.data == value:
                print("Values is found")
            elif rootNode.data>value:
                rootNode = rootNode.leftchild
            else:rootNode = rootNode.rightchild
        print("There is no such value in the tree")
                
## insertion
## There are two cases where first one is rotation is required and the other part is rotation is not required
        
#################################################################################################################################

new_avltree = AVLNode(None)