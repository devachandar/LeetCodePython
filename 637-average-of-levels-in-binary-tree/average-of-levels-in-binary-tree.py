# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        result = []
        queue = deque([root])

        while queue:
            len_queue = len(queue)
            sum_level = 0
            count = 0
            for _ in range(len_queue):
                node = queue.popleft()
                sum_level += node.val
                # count +=1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(sum_level/len_queue)
        
        return result
                 