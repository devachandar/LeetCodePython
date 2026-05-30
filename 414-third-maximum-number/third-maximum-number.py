class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        nums1=sorted(set(nums))
        if len(nums1)>=3:
            return nums1[-3]
        else:
            return max(nums)
        

        # first= sec= third = None

        # for num in nums:
        #     if num in (first,sec,third):
        #         continue
            
        #     if first is None or num > first:
        #         third = sec
        #         sec = first
        #         first = num

        #     elif sec is None or num > sec:
        #         third = sec
        #         sec = num
            
        #     elif third is None or num > third:
        #         third = num
            
        # if third is None:
        #     return first
        
        # return third