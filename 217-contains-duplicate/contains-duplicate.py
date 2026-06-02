class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = Counter(nums)

        for val in freq:
            if freq[val] >1:
                return True
            
        return False