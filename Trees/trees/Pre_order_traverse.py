import QueueLinkedList

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left_child = None
        self.right_child = None


Drinks= TreeNode("Drniks")
Hot = TreeNode("Hot")
Cold = TreeNode("Cold")
Hot1 = TreeNode("tea")
Hot2 = TreeNode("coffee")
alcoholic = TreeNode("Alcoholic")
non_alcohol = TreeNode("Non_Alcohol")


Drinks.left_child = Hot
Drinks.right_child = Cold
Hot.left_child = Hot1
Hot.right_child = Hot2
Cold.left_child = alcoholic
Cold.right_child = non_alcohol

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
def LevelOrderTravsersal(rootNode):
    if not rootNode:
        return
    else:
        tree_queue = QueueLinkedList.Queue()
        tree_queue.Enqueue(rootNode) # now the value inside a node in queue is a tree node. so before accesing tree node we need to mention node.value.leftchild or rightcjild
        
        while not(tree_queue.isEmpty()):
            root = tree_queue.Dequeue()
            print(root.value.data)
            if(root.value.left_child is not None):
                tree_queue.Enqueue(root.value.left_child)
            if(root.value.right_child is not None):
                tree_queue.Enqueue(root.value.right_child)
                
# FOR SEARCHING WE ARE USING LEVEL ORDER TRAVERSAL            
def Search_using_LevelOrder(Value,rootNode):
    if not rootNode:
        return
    else:
        tree_queue = QueueLinkedList.Queue()
        tree_queue.Enqueue(rootNode)
        while not(tree_queue.isEmpty()):
            root =tree_queue.Dequeue()
            if(root.value.data == Value):
                print(f'The value {Value} is found!!!!!!!!!!!')
                return 
            else:
                if(root.value.left_child is not None):
                    tree_queue.Enqueue(root.value.left_child)
                if(root.value.right_child is not None):
                    tree_queue.Enqueue(root.value.right_child)      
        print("Sorry !!!!!! The value is not found in the tree")
        return         
    
    
def Add_Value_To_tree(rootNode,value):
    new_node = TreeNode(value)
    if not rootNode:
        newTree = new_node
    else:
        tree_queue = QueueLinkedList.Queue()
        tree_queue.Enqueue(rootNode)
        while not(tree_queue.isEmpty()):
            root = tree_queue.Dequeue()
            if(root.value.left_child is None):
                root.value.left_child = new_node
                break
            else:tree_queue.Enqueue(root.value.left_child)
                
            if(root.value.right_child is None):
                root.value.right_child = new_node
                break
            else:tree_queue.Enqueue(root.value.right_child)
        LevelOrderTravsersal(rootNode)

# DELETING NODE : NEED TO FIND OUT THE LAST DEEPEST NODE : 
# TO FIND LAST DEEPEST NODE WE ARE USING LEVEL ORDER TRAVERSAL

def DeepesetNode(rootNode):
    if not rootNode:
        return
    else:
        tree_queue = QueueLinkedList.Queue()
        tree_queue.Enqueue(rootNode)
        
        while not(tree_queue.isEmpty()):
            temp = tree_queue.Dequeue()
            if (temp.value.left_child is not None):
                tree_queue.Enqueue(temp.value.left_child)
            if (temp.value.right_child is not None):
                tree_queue.Enqueue(temp.value.right_child)
        deepestNode = temp.value
        return deepestNode
        

def DeleteDeepesetNode(rootNode,deepestNode):
    if not rootNode:
        return
    else:
        tree_queue = QueueLinkedList.Queue()
        tree_queue.Enqueue(rootNode)
        while not (tree_queue.isEmpty()):
            root = tree_queue.Dequeue()
            if root.value == deepestNode:
                root.value = None
            
            if (root.value.left_child is not None):
                if(root.value.left_child == deepestNode):
                    root.value.left_child=None
                else:tree_queue.Enqueue(root.value.left_child)
            if( root.value.right_child is not None):
                if(root.value.right_child == deepestNode):
                    root.value.right_child = None
                else:tree_queue.Enqueue(root.value.right_child)

def DeleteNodeBinaryTree(rootNode,node):
    if not rootNode:
        return
    else:
        tree_queue = QueueLinkedList.Queue()
        tree_queue.Enqueue(rootNode)
        deepNode = DeepesetNode(rootNode)
        while not(tree_queue.isEmpty()):
            root = tree_queue.Dequeue()
            if root.value.data == node:
                dNode = DeepesetNode(rootNode)
                root.value.data = dNode.data
                DeleteDeepesetNode(rootNode,dNode)
                return "The node has been Susscefully deleted."
            if(root.value.left_child is not None):
                tree_queue.Enqueue(root.value.left_child)
            if(root.value.right_child is not None):
                tree_queue.Enqueue(root.value.right_child)
        return "The Node is not in the tree"
            

# DELETE THE ENTIRE BINARY TREE

def DeleteEntireBinaryTree(rootNode):
    rootNode.data = None
    rootNode.left_child = None
    rootNode.right_child = None        
    return "The tree is successfully deleted"      
                

        


###################################################################################################################################################

# LevelOrderTravsersal(Drinks)

# Search_using_LevelOrder("Cold1",Drinks)

# Add_Value_To_tree(Drinks,"MILO")

# DeleteNodeBinaryTree(Drinks,"tea")
# LevelOrderTravsersal(Drinks)
             
    

    
