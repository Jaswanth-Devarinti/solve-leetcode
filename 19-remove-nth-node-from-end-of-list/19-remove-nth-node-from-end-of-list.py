# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        pointer_one = head
        if pointer_one.next is None:
            pointer_one = None
            return pointer_one
        
        nth_node = head
        c = 0
        while(c<n):
            nth_node = nth_node.next
            c+=1
        
        pointer_one = head
        if pointer_one.next is None:
            pointer_one = None
            return pointer_one
        
        
        if nth_node is None:
            head = head.next
            return head
        
        
        while(nth_node.next is not None):
            pointer_one = pointer_one.next
            nth_node = nth_node.next
            
        pointer_one.next = pointer_one.next.next
        
        return head