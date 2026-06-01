class Solution:
    def rotateString(self, s: str, goal: str) -> bool:


        if len(s) != len(goal):
            return False
        s = s + s
        return s.find(goal) != -1
        
        # if len(s) != len(goal):
        #     return False

        # for i in range(len(s)):
        #     if s[i:len(s)] + s[:i] == goal:
        #         return True

        # return False
        
