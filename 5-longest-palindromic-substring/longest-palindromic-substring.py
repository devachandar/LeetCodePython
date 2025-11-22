class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s

        start, end = 0, 0  # indices of best palindrome

        def expand_from_center(left: int, right: int) -> (int, int):
            # expand as long as it's a valid palindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # when the while loop stops, left and right are one step beyond
            # the last valid palindrome, so actual palindrome is (left+1, right-1)
            return left + 1, right - 1

        for i in range(len(s)):
            # Odd-length center at i
            l1, r1 = expand_from_center(i, i)
            # Even-length center between i and i+1
            l2, r2 = expand_from_center(i, i + 1)

            # Pick the longer of the two
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]
