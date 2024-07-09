class BinaryHeap:
    def __init__(self,sizeof):
        self.customList=(sizeof+1)*[None] #[None, None, None, None, None, None, None]
        self.heapSize = 0
        self.maxSize = sizeof+1
        

def peakOfheap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.customList[1]

def sizeOfHeap(rootNode):
    if not rootNode:
        return
    else:return rootNode.heapSize
    
def LevelOrderTraversal(rootNode):
    #This is a list so the level order is just traversing through the list
    
    if not rootNode:
        return
    for x in rootNode.customList:
        print(x,end=" ")
        
#Heapify the binary tree if the binary properties are not satisfied
def HeapifyBeforeInsert(rootNode,index,heapType):
    parent_index = int(index/2)
    if index<=1:
        return  # there is nothing to heapify when there is only one element or there are no element
    if heapType == "Min":
        if rootNode.customList[index]<rootNode.customList[parent_index]:#in min heap parent should be lower than childs
            #swap
            rootNode.customList[index],rootNode.customList[parent_index] = rootNode.customList[parent_index],rootNode.customList[index]
        HeapifyBeforeInsert(rootNode,parent_index,heapType)
    elif heapType =="Max":
        if rootNode.customList[index] > rootNode.customList[parent_index]:
            #swap
            rootNode.customList[index],rootNode.customList[parent_index]=rootNode.customList[parent_index],rootNode.customList[index]
        HeapifyBeforeInsert(rootNode,parent_index,heapType)
            
        
def InserttoBinaryHeap(rootNode,value,heapType):
    if rootNode.heapSize+1 == rootNode.maxSize:
        return "The heap is full"
    rootNode.customList[rootNode.heapSize+1]=value
    rootNode.heapSize+=1
    #Then we need to heapify the list
    
    HeapifyBeforeInsert(rootNode,rootNode.heapSize,heapType)
    return "The value is added"
        
def heapifyTreeExtract(rootNode,index,heapType):
    left_index = 2*index
    right_index = 2*index+1
    swapChild= 0
    
    if rootNode.heapSize<left_index:
        return
    elif rootNode.heapSize == left_index: # here is for if we only have left child for the root node
        if heapType=="Min":
            if rootNode.customList[index]>rootNode.customList[left_index]:
                #then those two values should be swaped
                rootNode.customList[index],rootNode.customList[left_index] = rootNode.customList[left_index],rootNode.customList[index]
            return
        elif heapType == "Max":
            if rootNode.customList[index]<rootNode.customList[left_index]:
                #then those two values should be swaped
                rootNode.customList[index],rootNode.customList[left_index] = rootNode.customList[left_index],rootNode.customList[index]
            return
            
    else: # when root node has both left and right child we need to get min value out of tose two values for min heap and max value out of those to get the max heap
        if heapType == "Min":
            if left_index<right_index:
                swapChild = left_index
            else:swapChild = right_index
            if rootNode.customList[index]>rootNode.customList[swapChild]:
                #then those two values should be swaped
                rootNode.customList[index],rootNode.customList[swapChild] = rootNode.customList[swapChild],rootNode.customList[index]
            
        elif heapType =="Min":
            if left_index.right_index:
                swapChild = left_index
            else:swapChild = left_index
            if rootNode.customList[index]<rootNode.customList[swapChild]:
                #then those two values should be swaped
                rootNode.customList[index],rootNode.customList[swapChild] = rootNode.customList[swapChild],rootNode.customList[index]
        heapifyTreeExtract(rootNode,swapChild,heapType)

def ExtractMethod(rootNode,heapType):
    if rootNode.heapSize==0:
        return
    else:
        extactValue = rootNode.customList[1]
        rootNode.customList[1]=rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize]=None
        rootNode.heapSize -=1
        heapifyTreeExtract(rootNode,1,heapType)
        return extactValue
def DeleteHeap(rootNode):
    rootNode.customList = None

##################################################################################################################################
        

binaryheap = BinaryHeap(6)
# print(peakOfheap(binaryheap))
# print(sizeOfHeap(binaryheap))


InserttoBinaryHeap(binaryheap,4,"Min")

InserttoBinaryHeap(binaryheap,5,"Min")
InserttoBinaryHeap(binaryheap,34,"Min")
InserttoBinaryHeap(binaryheap,114,"Min")
InserttoBinaryHeap(binaryheap,54,"Min")
print(ExtractMethod(binaryheap,"Min"))
print(ExtractMethod(binaryheap,"Min"))
print(ExtractMethod(binaryheap,"Min"))
print(sizeOfHeap(binaryheap))
LevelOrderTraversal(binaryheap)
        