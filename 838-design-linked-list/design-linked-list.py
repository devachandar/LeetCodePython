class Node:
    def __init__(self,val=0):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.sentinel = Node(0)
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.sentinel.next
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size,val)


    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        new_node = Node(val)
        curr = self.sentinel
        for _ in range(index):
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node
        self.size +=1


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        curr = self.sentinel
        for _ in range(index):
            curr = curr.next
        curr.next = curr.next.next
        self.size -=1















# class Node:
#     def __init__(self,val=0):
#         self.val = val
#         self.next = None

# class MyLinkedList:
#     def __init__(self):
#         self.head = None

#     def get(self, index: int) -> int:
#         curr = self.head
#         for _ in range(index):
#             curr = curr.next
#         return curr.val

#     def addAtHead(self, val: int) -> None:
#         new_node = Node(val)
#         new_node.next = self.head
#         self.head = new_node

#     def addAtTail(self, val: int) -> None:
#         new_node = Node(val)
#         curr = self.head
#         while curr.next:
#             curr = curr.next
        
#         curr.next = new_node


#     def addAtIndex(self, index: int, val: int) -> None:
#         new_node = Node(val)
#         curr = self.head
#         for _ in range(index-1):
#             curr = curr.next
#         new_node.next = curr.next
#         curr.next = new_node


#     def deleteAtIndex(self, index: int) -> None:
        
#         curr = self.head
#         for _ in range(index-1):
#             curr = curr.next
#         curr.next = curr.next.next



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)