from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # 1. Find the first decreasing element from the right
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # 2. Find element just larger than nums[i] from the right
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            # 3. Swap them
            nums[i], nums[j] = nums[j], nums[i]

        # 4. Reverse the suffix
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
