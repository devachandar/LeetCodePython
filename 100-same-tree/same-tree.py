# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        first_tree = self.levelTree(p)
        second_tree = self.levelTree(q)

        # print(first_tree)
        # print(second_tree)
        return first_tree == second_tree


    def levelTree(self,root): 
     
        result = []
        queue = deque([root])
        if not root:
            return result
        
        while queue:
            node = queue.popleft()
            # result.append(node.val)
            if node != "null":
                result.append(node.val)
                if node.left:
                    queue.append(node.left)
                else:
                    queue.append("null")
                if node.right:
                    queue.append(node.right)
                else:
                    queue.append("null")
            else:
                result.append("null")

        return result

