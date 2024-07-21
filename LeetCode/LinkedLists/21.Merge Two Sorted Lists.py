# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    

    def create_LL(self,l):
        if not l:
            return None
        print(l)
        new_node = ListNode(l[0])
        head = new_node
        tail = new_node
        

        if l[1:]:
            for x in l[1:]:
                newNode = ListNode(x)
                tail.next = newNode
                tail = tail.next
        return head

        
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def toList(node ,l = None):
            if l is None:
                l = []
            while node is not None:
                l.append(node.val)
                node = node.next
            return l
        l1 = toList(list1)
        l2 = toList(list2)
        result = l1+l2
        result.sort()
        print(result)
        #print(self.create_LL(result))
        return self.create_LL(result)
    
#######################################################################################################################$#####
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = ListNode()
        ptr3 = list3
        while(list1!=None or list2!=None):
            if((list1!=None) and (list2!=None)):
                if(list1.val == list2.val):
                    current = ListNode(list1.val)
                    ptr3.next = current
                    ptr3 = ptr3.next
                    list1 = list1.next
                elif (list1.val < list2.val):
                    current = ListNode(list1.val)
                    ptr3.next = current
                    ptr3 = ptr3.next
                    list1 = list1.next
                elif (list2.val < list1.val):
                    current = ListNode(list2.val)
                    ptr3.next = current
                    ptr3 = ptr3.next
                    list2 = list2.next
            elif(list1!=None):
                current = ListNode(list1.val)
                ptr3.next = current
                ptr3 = ptr3.next
                list1 = list1.next
            elif(list2!=None):
                current = ListNode(list2.val)
                ptr3.next = current
                ptr3 = ptr3.next
                list2 = list2.next

        return list3.next
    