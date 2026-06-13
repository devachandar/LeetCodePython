class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        prefix = [0] * (len(nums)+1)

        for i in range(len(nums)):
            # prefix[i] = prefix[i-1]+ nums[i]
            prefix[i + 1] = prefix[i] + nums[i]

        print(prefix)
        for i in range(1,len(nums)+1):
            if prefix[i-1] == (prefix[len(nums)] - prefix[i]):
                return i-1

        return -1