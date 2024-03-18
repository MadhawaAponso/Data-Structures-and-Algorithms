class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left_child = None
        self.right_child = None


Drinks= TreeNode("Drniks")
Hot = TreeNode("Hot")
Cold = TreeNode("Cold")
Hot1 = TreeNode("Hot1")

Drinks.left_child = Hot
Drinks.right_child = Cold
Hot.left_child = Hot1

def Preorder_traversal(rootNode):
    if not  rootNode:
        return
    print(rootNode.data)
    Preorder_traversal(rootNode.left_child)
    Preorder_traversal(rootNode.right_child)

def Inorder_traversal(rootNode):
    if not rootNode:
        return 
    Inorder_traversal(rootNode.left_child)
    print(rootNode.data)
    Inorder_traversal(rootNode.right_child)

def postorder_traversal(rootNode):
    if not rootNode:
        return 
    Inorder_traversal(rootNode.left_child)
    Inorder_traversal(rootNode.right_child)
    print(rootNode.data)
    
# For level traversal we need to have queue

    
Preorder_traversal(Drinks)