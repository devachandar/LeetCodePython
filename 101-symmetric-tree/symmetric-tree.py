# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        left_preorder = self.preOrder(root.left,"Left")
        # print(left_preorder)
        right_preorder = self.preOrder(root.right,"Right")

        return left_preorder == right_preorder

    def preOrder(self,root,side):

        result = []

        if not root:
            return result
        
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node != "null":
                result.append(node.val)
                if side == "Left":
                    if node.left:
                        queue.append(node.left)
                    else:
                        queue.append("null")
                    if node.right:
                        queue.append(node.right)
                    else:
                        queue.append("null")
                else:
                    if node.right:
                        queue.append(node.right)
                    else:
                        queue.append("null")
                    if node.left:
                        queue.append(node.left)
                    else:
                        queue.append("null")
            else:
                result.append("null")
        return result
            
