class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        def is_palindrome(left,right):
            while left< right:
                if s[left] != s[right]:
                    return False
                else:
                    left+=1
                    right-=1
            return True


        while left < right:
            if s[left] != s[right]:
                return (
                    is_palindrome(left + 1, right) or
                    is_palindrome(left, right - 1)
                )
            else:
                left+=1
                right-=1
        
        return True

        #     if s[left] != s[right] and count == 0:
        #         if s[left] == s[right-1]:
        #             right-=1
        #             count+=1
        #         elif s[left+1] == s[right]:
        #             left+=1
        #             count+=1
        #         else:
        #             return False
        #     elif s[left] == s[right]:
        #         left+=1
        #         right-=1
        #     else:
        #         return False

        # return True