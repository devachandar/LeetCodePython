class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            nums.append(target)
            nums = sorted(nums)
            return nums.index(target)