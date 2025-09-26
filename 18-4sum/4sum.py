class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if nums[i] == nums[i-1] and i!=0:
                continue
            left = i
            right=(len(nums)-1)
            middle = left + 1
            while left<right:
                left+=1

                if nums[left] == nums[left-1] and left-1!=i:
                    continue
                
                middle = left + 1
                right = len(nums)-1
                
                # print(nums[left],nums[middle],nums[right])
                # print("dd",left,middle,right)
                while middle <right:
                    sum = nums[i]+ nums[left]+nums[right]+nums[middle]
                    # print("dd",nums[i],nums[left],nums[middle],nums[right])
                    if sum == target:
                        result.append([nums[i],nums[left],nums[middle],nums[right]])
                        middle+=1
                        right-=1

                        while middle<right and nums[middle] == nums[middle-1]:
                            middle+=1

                        while middle<right and nums[right] == nums[right+1]:
                            right-=1
                    
                    elif sum < target:
                        middle+=1
                        while middle<right and nums[middle] == nums[middle-1]:
                            middle+=1
                    
                    else :
                        right-=1
                        while middle<right and nums[right] == nums[right+1]:
                            right-=1
                
                

        return result
