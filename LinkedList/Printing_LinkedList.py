class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

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