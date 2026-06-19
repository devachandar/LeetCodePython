# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next

            # Rewire the three pointers
            prev.next = second
            first.next = second.next
            second.next = first

            # Advance prev to the end of the swapped pair
            prev = first

        return dummy.next
        # dummy = ListNode(0,head)
        # curr = dummy
        # while curr:
        #     if curr.next and curr.next.next:
        #         temp = curr.next.next
        #         curr_next_next_next = curr.next.next.next
        #         curr_next = curr.next
        #         curr.next.next = curr_next_next_next
        #         curr.next.next.next = curr_next
            
        #         curr.next = temp

        #         curr = curr.next.next
        #     else:
        #         curr = curr.next

        