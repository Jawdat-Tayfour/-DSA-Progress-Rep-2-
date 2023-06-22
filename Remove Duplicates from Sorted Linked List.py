# My Solution ^_^
class ListNode():
    def __init__(self,value=None,next=None):
        self.value = value 
        self.next = next
def RDFSLL(head:ListNode)-> ListNode:
    if not head or not head.next :
        return None
    current,prev = head.next,head
    while current:
        if current.value != prev.value : 
            prev = current
        else: 
            if not current.next:
                prev.next = None 
            else :
                prev.next = current.next
        current = current.next                        

    return head     
#O(n) Time complexity ^_^ , I tested it and it works my fella ^__^, I didn't even watch the explaination yet. OMGGGGGGG.
#Neet Code Solution. 
def RDFSLL2(head:ListNode) -> ListNode:
    cur = head 
    while cur:
        while cur.next and cur.value == cur.next.value :
            cur.next = cur.next.next 
        cur = cur.next
    return head     
# O(n) Time complexity, but he did it in 5 lines code, as usual, I can't beat the master lmao. 

# Create a sorted linked list with duplicates
head = ListNode(2)
node2 = ListNode(2)
node3 = ListNode(2)
node4 = ListNode(3)
node5 = ListNode(3)



head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = None 

# Test the RDFSLL/RDFSLL2 function
modified_head = RDFSLL2(head)
current = modified_head
while current:
    print(current.value, end=" -> ")
    current = current.next
print("None")
