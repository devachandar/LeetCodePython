class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        k=0
        for num in nums:
            if k<2 or num!=nums[k-2]:
                nums[k]=num
                k+=1
        return k
        
        
        # sub_count = 1

        # i = 0       
        # while i < len(nums) - 1:
        #     if nums[i] != nums[i + 1]:
        #         sub_count = 0
        #     sub_count += 1

        #     if sub_count > 2:
        #         nums.remove(nums[i])
        #         i -=1
        #     i += 1

            
        