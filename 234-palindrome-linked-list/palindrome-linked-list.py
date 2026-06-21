# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        val_list = []

        curr = head
        while curr:
            val_list.append(curr.val)
            curr = curr.next
        
        if val_list == val_list[::-1]:
            return True
        else:
            return False