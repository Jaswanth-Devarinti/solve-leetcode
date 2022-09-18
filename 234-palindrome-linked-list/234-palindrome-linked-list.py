# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ans = ''
        point = head
        while(point is not None):
            ans += str(point.val)
            point = point.next
        
        if ans == ans[::-1]:
            return True
        return False