class Solution:
    def isPalindrome(self, s: str) -> bool:


        left, right = 0, len(s) - 1
        s = s.lower()

        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1

        return True
        
        # left = 0 
        # right = len(s) - 1
        # s = s.lower()
        # while left<right:
        #     if not (('0' <= s[left] <= '9') or ('a' <= s[left] <= 'z')):
        #         left +=1
        #     elif not (('0' <= s[right] <= '9') or ('a' <= s[right] <= 'z')):
        #         right -=1
        #     elif s[left] != s[right]:
        #         print(s[left],s[right],left,right)
        #         return False
        #     else:
        #         left +=1
        #         right -=1
        
        # return True