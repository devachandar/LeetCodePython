class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        stack = []
        third = float('-inf')  # Best candidate for nums[k] (the "2" in 132)

        # Iterate from right to left
        for i in range(n - 1, -1, -1):
            # If current element is less than third, we found the "1"
            if nums[i] < third:
                return True

            # Pop elements smaller than current; they become candidates for "2"
            while stack and nums[i] > stack[-1]:
                third = max(third, stack.pop())
            stack.append(nums[i])

        return False