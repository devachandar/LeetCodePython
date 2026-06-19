# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        size = 0
        while curr:
            curr= curr.next
            size+=1
        # print(size)
        curr = dummy
        for _ in range(size-1-n):
            curr = curr.next
            print(curr.val)
        
        # print("cc",curr.val)
        curr.next = curr.next.next
        
        return dummy.next