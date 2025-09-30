class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i=0
        while i<n:
            if (nums[i]==val):
                nums.remove(nums[i])
            else:
                i+=1
            n = len(nums)
            
        return len(nums)