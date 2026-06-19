# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        unique = set()
        list_to_remove = set()

        curr = head
        while curr:
            
            if curr.val in unique:
                list_to_remove.add(curr.val)
            unique.add(curr.val)
            curr = curr.next

        dummy = ListNode(0,head)

        curr = dummy

        while curr.next:
            if curr.next.val in list_to_remove:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next
        # print(unique,list_to_remove)

        # unique = set()
        # if head:
        #     unique.add(head.val)
        # else:
        #     return []

        # curr = head
        # while curr.next:
        #     if curr.next.val in unique:
        #         curr.next = curr.next.next
        #     else:
        #         unique.add(curr.next.val)
        #         curr = curr.next
        
        # return head