class Node:
    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head_sentinel = Node(0)
        self.tail_sentinel = Node(0)
        self.head_sentinel.next = self.tail_sentinel
        self.tail_sentinel.prev = self.head_sentinel
        self.size = 0

    def _get_node_at(self, index: int) -> Node:
        if index < self.size // 2:
            node = self.head_sentinel.next
            for _ in range(index):
                node = node.next
        else:
            node = self.tail_sentinel.prev
            for _ in range(self.size - 1 - index):
                node = node.prev
        return node

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        return self._get_node_at(index).val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)
        # new_node = Node(val)
        # after = self.head_sentinel.next
        # self.head_sentinel.next = new_node
        # new_node.prev = self.head_sentinel
        # new_node.next = after
        # after.prev = new_node
        # self.size += 1

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size,val)
        # new_node = Node(val)
        # before = self.tail_sentinel.prev
        # before.next = new_node
        # new_node.prev = before
        # new_node.next = self.tail_sentinel
        # self.tail_sentinel.prev = new_node
        # self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == self.size:
            successor = self.tail_sentinel
            predecessor = self.tail_sentinel.prev
        else:
            successor = self._get_node_at(index)
            predecessor = successor.prev
        new_node = Node(val)
        new_node.prev = predecessor
        new_node.next = successor
        predecessor.next = new_node
        successor.prev = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        node = self._get_node_at(index)
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

# class Node:
#     def __init__(self,val=0):
#         self.val = val
#         self.next = None

# class MyLinkedList:
#     def __init__(self):
#         self.sentinel = Node(0)
#         self.size = 0

#     def get(self, index: int) -> int:
#         if index < 0 or index >= self.size:
#             return -1
#         curr = self.sentinel.next
#         for _ in range(index):
#             curr = curr.next
#         return curr.val

#     def addAtHead(self, val: int) -> None:
#         self.addAtIndex(0,val)

#     def addAtTail(self, val: int) -> None:
#         self.addAtIndex(self.size,val)


#     def addAtIndex(self, index: int, val: int) -> None:
#         if index < 0 or index > self.size:
#             return
#         new_node = Node(val)
#         curr = self.sentinel
#         for _ in range(index):
#             curr = curr.next
#         new_node.next = curr.next
#         curr.next = new_node
#         self.size +=1


#     def deleteAtIndex(self, index: int) -> None:
#         if index < 0 or index >= self.size:
#             return
#         curr = self.sentinel
#         for _ in range(index):
#             curr = curr.next
#         curr.next = curr.next.next
#         self.size -=1















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