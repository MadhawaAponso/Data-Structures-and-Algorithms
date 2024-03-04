class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Cir_LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def Append(self, value):
        new_node = Node(value) # create a new node

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head  
        else:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head 

        self.length += 1
    
    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head 
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
        self.length+=1
    
    def Insert(self , value , index):
        if index < 0 or index > self.length:
            print("Out of Range")
            return -1
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
        



            



