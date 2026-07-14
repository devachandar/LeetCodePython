# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        if not root:
            return []

        result = []
        # Stack stores pairs of (node, path string so far)
        stack = [(root, str(root.val))]

        while stack:
            node, path = stack.pop()

            # If it's a leaf, save the path
            if not node.left and not node.right:
                result.append(path)
                continue

            # Push children with extended paths
            if node.right:
                stack.append((node.right, path + "->" + str(node.right.val)))
            if node.left:
                stack.append((node.left, path + "->" + str(node.left.val)))

        return result