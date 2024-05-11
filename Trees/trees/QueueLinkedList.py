
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    def __str__(self):
        return str(self.value)
        

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0
    
    # Here we make our linked list iterable. now it can be iterarte through the linked list like a normal list
    def __iter__(self): # This funtion is for iterating over the linked list. and yeilding means it gives the value
        curNode = self.head
        while(curNode):
            yield curNode
            curNode = curNode.next
            
            
class Queue:
    def __init__(self):
        self.linkedlist = LinkedList()
    
    def __str__(self):
        values = [str(x) for x in self.linkedlist]
        return " ".join(values)
    
    def Enqueue(self,value):
        newNode = Node(value)
        if(self.linkedlist.head == None):
            self.linkedlist.head = newNode
            self.linkedlist.tail = newNode
        else:
            self.linkedlist.tail.next = newNode
            self.linkedlist.tail = newNode
        self.linkedlist.len +=1
    
    def Dequeue(self):
        if (self.isEmpty()):
            return "The list is empty"
        else:
            temp = self.linkedlist.head
            if(self.linkedlist.len == 1):
                self.linkedlist.head = None
                self.linkedlist.tail = None
            else:
                self.linkedlist.head = self.linkedlist.head.next
            self.linkedlist.len -=1
            return temp
                
        
    def isEmpty(self):
        if(self.linkedlist.len ==0):
            return True
        else:return False
        
        
    def Peek(self):
        if self.isEmpty():
            return "The list is empty"
        else:
            return self.linkedlist.head
    
    

        
            
        


        