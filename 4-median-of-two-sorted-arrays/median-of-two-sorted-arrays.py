class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # total = 0

        # for i in nums1:
        #     total= total + i
        # for i in nums2:
        #     total+=i
        # print(total/(len(nums1)+len(nums2))) 
        # return total/(len(nums1)+len(nums2))
        merged = sorted(nums1 + nums2)
        n = len(merged)
        
        mid = n // 2
        
        if n % 2 == 1:  # odd length
            return float(merged[mid])
        else:           # even length
            return (merged[mid - 1] + merged[mid]) / 2