#in this one we are remving every occurrence of the a certain value in a linked list
class ListNode():
    def __init__(self,value,next):
        self.value = value 
        self.next = next 
def removeElements(head:ListNode,Nodetoremove:ListNode) -> ListNode : 
    dummy = ListNode(None,head)
    prev,curr = dummy , head 
    while curr:
        if curr.value == Nodetoremove.value:
            prev.next = curr.next 
        else:
            prev = curr 
        curr = curr.next     
    return dummy        
# O(n) complexity