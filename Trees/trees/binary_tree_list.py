# Create Binary tree using list


class BinaryTree:
    def __init__(self,size):
        self.customList = size * [None]  # this creates a list of all the values none with the size of size
        self.lastUsedIndex = 0
        self.maxIndex = size
        
    def insertNode(self,value):
        if (self.lastUsedIndex+1 == self.maxIndex):
            return "The tree is full"
        else:
            self.customList[self.lastUsedIndex+1]= value
            self.lastUsedIndex+=1
            return "The node is succesfully added"
        
    def SearchNode(self,value):
        for x in self.customList:
            if x == value:
                return "The value is found"
        return "Sorry!!!!!!! The value is not found"
    
    def PreOrderTraversal(self,index):
        #base case 
        if index>self.lastUsedIndex:
            return
        print(self.customList[index])
        self.PreOrderTraversal(index*2)# beacuse the left subtree
        self.PreOrderTraversal(index*2 + 1)
        
    def InorderTraversal(self, index):
        if index>self.lastUsedIndex:
            return
        self.PreOrderTraversal(index*2)# beacuse the left subtree
        print(self.customList[index])
        self.PreOrderTraversal(index*2 + 1)
        
    def PostOrderTraversal(self,index):
        if index>self.lastUsedIndex:
            return
        self.PreOrderTraversal(index*2)# beacuse the left subtree
        self.PreOrderTraversal(index*2 + 1)
        print(self.customList[index])
        
    def LevelOrderTraversal(self,index):
        for x in self.customList[index:]:
            print(x)
            
    def DeleteNode(self,value):
        if(self.lastUsedIndex==0):
            return("The tree is empty")
        else:
            for x in range(1,self.customList):
                if (self.customList[x] == value):
                    self.customList[x]= self.customList[self.lastUsedIndex]
                    self.customList[self.lastUsedIndex]=None
                    self.lastUsedIndex -=1
                    return "The Node is successfully deleted"
                
    def deletebinarytree(self):
        self.customList = None
        return "The binary tree is deleted"
                    
                        

#########################################################################################################################
 
newBT = BinaryTree(4)
newBT.insertNode(3)
newBT.insertNode(2)
newBT.insertNode(1)

print(newBT.customList)
newBT.InorderTraversal(1) # starts from the index 1 here

newBT.LevelOrderTraversal(1)


# print(newBT.SearchNode(7))