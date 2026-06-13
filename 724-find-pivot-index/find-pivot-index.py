class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        total_sum = sum(nums)

        left_sum = 0
        for i in range(len(nums)):
           
            right_sum = total_sum - left_sum - nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]

        return -1
        
        # prefix = [0] * (len(nums)+1)

        # for i in range(len(nums)):
        #     prefix[i + 1] = prefix[i] + nums[i]

        # for i in range(1,len(nums)+1):
        #     if prefix[i-1] == (prefix[len(nums)] - prefix[i]):
        #         return i-1

        # return -1