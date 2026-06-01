class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        index_of_fst_lt = 0 


        if len(s) != len(goal):
            return False

        for i in range(len(s)):
            if s[i:len(s)] + s[:i] == goal:
                return True

        return False
        
        
        # right = len(goal) - 1

        # while right > 0:
        #     if goal[right] == s[0]:
        #         index_of_fst_lt = right
        #         if right == 0:
        #             return False
        #         break
            
        #     right -=1

        # goal_left = goal[:right]
        # goal_right = goal[right:len(s)]

        # s_left = s[:len(s)-right]
        # s_right = s[len(s)-right : len(s)]

        # if s_left == goal_right and s_right == goal_left:
        #     return True
        # else:
        #     return False
