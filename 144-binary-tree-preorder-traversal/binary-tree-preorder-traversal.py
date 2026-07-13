# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        

        result = []
        queue = deque([root])
        if not root:
            return result

        while queue:
            node = queue.popleft()
            result.append(node.val)
            if node.right:
                queue.appendleft(node.right)
            if node.left:
                queue.appendleft(node.left)
            
        return result 

    #     result = []
    #     self._inorder(root,result)
    #     return result
    
    # def _inorder(self,node,result):
    #     if not node:
    #         return
    #     result.append(node.val)
    #     self._inorder(node.left,result)
    #     self._inorder(node.right,result)