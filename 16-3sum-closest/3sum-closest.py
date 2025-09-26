class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest_target = nums[0]+nums[1] + nums[2]
        nums.sort()
        
        for i in range(len(nums)):
            if nums[i] == nums[i-1] and i!=0:
                continue
            left = i + 1
            right = len(nums)-1

            while left<right:
                current_target = nums[i] + nums[left] + nums[right]
                if abs(current_target - (target)) < abs(closest_target -(target)):
                    closest_target = current_target
                    # left+=1
                    # right-=1
                if current_target < target:
                    left+=1
                else:
                    right-=1

            
        return closest_target
                