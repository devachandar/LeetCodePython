class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rotated_nums = []
        if k > len(nums):
            k = k % len(nums)
        for i in range(len(nums)-k,len(nums)):
            rotated_nums.append(nums[i])
        for i in range(len(nums)-k):
            rotated_nums.append(nums[i])
        nums[:] = rotated_nums
        