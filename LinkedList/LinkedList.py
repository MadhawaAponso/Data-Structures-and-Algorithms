class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # PRINTING THE LINKEDLIST
    def __str__(self):
        s = ""
        if self.length==0:
            s="LinkedList is Empty"
        else:
            temp = self.head
            while(temp is not None):
                s += str(temp.value)
                if(temp.next is not None):
                    s += "->"
                temp = temp.next
        return s
    

    # APPENDING TO THE LINKEDLIST
    def AppendToLinkedListAtTheEnd(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1
    
    # PREPENDING TO THE LINKEDLIST
    def AppendToLinkedListAtTheStart(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1
    
    # INSERTING TO THE LINKEDLIST FOR GIVEN INDEX
    def InsertToLinkedList(self,value,position):
        if position < 0 or position > self.length:
            print("Out of Range")
            return -1

        new_node = Node(value)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            for _ in range(position - 1):
                temp = temp.next

            new_node.next = temp.next
            temp.next = new_node

        self.length += 1
    
    #TRAVERSING THE LINKEDLIST
    def Traverse(self):
        if self.head is None:
            print("There is no value")
        else:
            current = self.head
            number = 1
            while(current!=None):
                print(f"{[number]} : {current.value}")
                current = current.next
                number = number + 1
    
    
    # SEARCHING THE LINKEDLIST BY THERE VALUES
    def Search_By_Value(self, value):
        if self.head is None:return False
        else:
            current = self.head
            while(current!=None):
                if(current.value == value):return True
                current = current.next
            return False
    
    def Get(self,index): # different method for this
        pass
    def Set(self,value,index): # different method for this
        current = self.head
        for x in range(index):
            current = current.next
        current.value = value
    
    def PopFirstNode(self):
        popped_node = self.head
        if self.head == None:
            return None
        elif self.length == 1 : 
            self.head = None
            self.tail = None
        else:
            self.head = popped_node.next
            popped_node.next = None
        self.length -=1
        return popped_node
    
    def PopLastElement(self): # diiferent code than this
        current_node = self.head
        current_node_after = None
        if self.head is None:
            return False
        elif self.length == 1 :
            self.head = None
            self.tail = None
            
        else:
            while(current_node.next is not None):
                current_node_after = current_node
                current_node = current_node.next
            self.tail = current_node_after
            current_node_after.next = None
        self.length-=1
        return current_node.value
    
    def remove_given_index(self, index):
        pass


my_lsit = LinkedList()
my_lsit.AppendToLinkedListAtTheEnd(10)
my_lsit.AppendToLinkedListAtTheEnd(12)
my_lsit.AppendToLinkedListAtTheStart(1212)
my_lsit.InsertToLinkedList(3,0)
my_lsit.Traverse()
print(my_lsit.PopLastElement())

print(my_lsit)

