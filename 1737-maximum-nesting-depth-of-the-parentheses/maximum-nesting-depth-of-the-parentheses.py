class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        result = 0
        for ch in s:
            if ch == "(":
                stack.append(ch)
                result = max(result,len(stack))
            elif ch == ")":
                stack.pop()
        
        return result