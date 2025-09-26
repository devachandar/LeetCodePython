# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         target = set()
#         for i in range(len(nums)-2):
#             for j in range(i+1,len(nums)-1):
#                 for k in range(j+1,len(nums)):
#                     # if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
#                     if (nums[i] +nums[j] + nums[k] == 0):
#                         target.add(tuple(sorted([nums[i],nums[j],nums[k]])))

#         return list(target)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result= []
        for i in range(len(nums)):
            if nums[i] == nums[i-1] and i!=0:
                continue
            left = i+1
            right = len(nums)-1
            while left<right:
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    result.append([nums[i] , nums[left] , nums[right]])
                    left+=1
                    right-=1

                    while left<right and nums[left] == nums[left-1]:
                        left+=1
                    
                    while left<right and nums[right] == nums[right+1]:
                        right-=1
                elif s < 0:
                    left+=1
                else:
                    right-=1
        return result


