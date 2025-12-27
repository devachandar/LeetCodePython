class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n   # important!

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # Step 1: reverse entire array
        reverse(0, n - 1)

        # Step 2: reverse first k elements
        reverse(0, k - 1)

        # Step 3: reverse remaining elements
        reverse(k, n - 1)



        # Using extra variable
        # rotated_nums = []
        # if k > len(nums):
        #     k = k % len(nums)
        # for i in range(len(nums)-k,len(nums)):
        #     rotated_nums.append(nums[i])
        # for i in range(len(nums)-k):
        #     rotated_nums.append(nums[i])
        # nums[:] = rotated_nums
        