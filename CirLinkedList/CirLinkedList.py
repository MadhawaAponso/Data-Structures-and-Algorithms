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
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head  
        else:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head 

        self.length += 1
    def __str__(self):
        if self.length == 0:
            return "The list is empty"
        else:
            _string = ""
            temp = self.head
            while temp is not None:
                _string += str(temp.value)
                temp = temp.next
                if temp == self.head:
                    break
                _string+="->"
        return _string

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
            if self.head is None:
                self.head = new_node
                self.tail = new_node
                new_node.next = self.head
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = self.head
        elif index ==self.length:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail =new_node
        else:
            temp = self.head
            prev_temp = None
            for i in range(index-1):
                prev_temp = temp
                temp = temp.next
            prev_temp.next = new_node
            new_node.next = temp
        self.length += 1

    def Remove():
        pass
    def Traverse(self):
        count = 0
        current_node = self.head
        while current_node is not None:
            count += 1
            print(f"{count} : {current_node.value}")
            current_node = current_node.next
            if current_node == self.head:
                break
    def Search(self,value):
        temp_node = self.head
        count = 1
        while temp_node.value != value:
            count +=1
            temp_node = temp_node.next
            if temp_node == self.head:
                return "The value doesnt exist"
        return f"The value exist at index : {count}"

    def pop_first(self):
        pass
    def pop_last(self):
        pass
        



            


new_linkedlist = Cir_LinkedList()
new_linkedlist.Append(1)
new_linkedlist.Append(2)
new_linkedlist.prepend(0)
new_linkedlist.Append(3)
new_linkedlist.Append(4)
new_linkedlist.Append(5)
new_linkedlist.Append(6)
new_linkedlist.Insert(99,0)
new_linkedlist.Traverse()
print(new_linkedlist.Search(9))

print(new_linkedlist)