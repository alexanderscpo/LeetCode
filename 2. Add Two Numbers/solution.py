# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1 = ''
        c2 = ''
        
        while l1 is not None:
            c1 += str(l1.val)
            l1 = l1.next
            
        while l2 is not None:
            c2 += str(l2.val)
            l2 = l2.next
            
        aux = str(int(c1[::-1]) + int(c2[::-1]))
        result = ListNode()
        cursor = result
        t = 1
        
        for i in reversed(aux):  
            if t == 1:
                cursor.val = int(i)
                t-=1
             
            else:
                while cursor.next is not None:
                    cursor = cursor.next
                cursor.next = ListNode(int(i))
        
        return result