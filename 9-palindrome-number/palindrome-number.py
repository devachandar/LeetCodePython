class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = str(x)[::-1]
        print("d",rev)
        if str(x) == rev:
            return True
        else:
            return False