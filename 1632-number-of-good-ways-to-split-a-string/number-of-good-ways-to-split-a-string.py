class Solution:
    def numSplits(self, s: str) -> int:

        right = Counter(s)
        left = set()
        good_splits = 0

        for ch in s[:-1]:  # last split is invalid
            left.add(ch)
            right[ch] -= 1
            if right[ch] == 0:
                del right[ch]

            if len(left) == len(right):
                good_splits += 1

        return good_splits


        # n = len(s)
        # count = 0
        # i = int(n/2)
        # while i<n:
        #     if len(Counter(s[:i])) == len(Counter(s[i:])):
        #         count+=1

        #     i+=1
        
        # i = int(n/2)-1
        # while i>=0:
        #     if len(Counter(s[:i])) == len(Counter(s[i:])):
        #         count+=1
        #     i -=1
        
        # return count
        


