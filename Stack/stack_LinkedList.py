class Node:
    def __init__(self , value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


class Stack_Linkedlist:
    def __init__(self):
        self.linkedlist = LinkedList()
        
    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1
    
    def pop(self):
        if self.head is None:
            return "The list is empty"
        elif self.length == 1:
            popvalue = self.head.value
            self.head = None
            self.tail=None
        else:
            temp = self.head
            popvalue = self.head.value
            self.head= self.head.next
            temp.next = None
        self.length -=1
        return popvalue
    
    def isEmpty(self):
        if self.length == 0:
            return True
        else:return False
    
    def delete(self):
        self.head == None
        self.tail==None
        self.length  = None
    
    def Peek(self):
        temp = self.head
        while(temp.next is not None):
            temp = temp.next
        return temp.value

            


