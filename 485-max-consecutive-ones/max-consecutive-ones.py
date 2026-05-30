class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        sub_count = 0
        

        for num in nums:
            if num == 1:
                sub_count +=1
            else:
                sub_count = 0
            
            max_count = max(max_count,sub_count)

        return max_count