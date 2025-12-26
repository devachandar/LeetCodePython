class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # nums = set(nums)
        # return len(nums)


        n = len(nums)
        i=0
        while i<n-1:
            if(nums[i]==nums[i+1]):
                nums.remove(nums[i+1])
            else:
                i+=1
            n = len(nums)
            
        return len(nums)