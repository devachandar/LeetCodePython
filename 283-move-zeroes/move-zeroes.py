class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # insert_pos = 0

        # # Step 1: Move all non-zero elements to the front
        # for num in nums:
        #     if num != 0:
        #         nums[insert_pos] = num
        #         insert_pos += 1

        # # Step 2: Fill remaining positions with 0
        # while insert_pos < len(nums):
        #     nums[insert_pos] = 0
        #     insert_pos += 1
            
        for i in range(len(nums)):
            if nums[i] == 0:
                for j in range(i+1,len(nums)):
                    if nums[j] != 0:
                        nums[i] = nums[j]
                        nums[j] = 0
                        break
        