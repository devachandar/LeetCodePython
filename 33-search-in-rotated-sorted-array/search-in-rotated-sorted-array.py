class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # half = len(nums) // 2
        # reverted_nums = nums[half:]
        # reverted_nums+=nums[:half]
        try:
            index = nums.index(target)
            print(index)
            return index
        except:
            return -1