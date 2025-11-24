class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0
        max_len = 0 
        def expand(left:int,right:int):

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -=1
                right +=1
            
            return left+1, right-1 

        for i in range(len(s)):
            l1, r1 = expand(i,i)
            l2, r2 = expand(i,i+1)
            
            if r1-l1+1 > max_len:
                max_len =r1-l1+1
                start = l1
                end = r1
            if r2-l2+1 > max_len:
                max_len = r2-l2+1
                print("max",max_len,r2,l2)
                start = l2
                end = r2
        
        return s[start:end+1]
