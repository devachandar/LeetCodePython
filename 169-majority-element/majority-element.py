class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        nums.sort()
        count = 0
        max_count = 0
        candidate = nums[0]

        for i in range(0,len(nums)-1):
            if nums[i] != nums[i+1]:
                if count > max_count:
                    max_count = count
                    candidate = nums[i]
            
                count = 0
            else:
                count+=1
        if count > max_count:
            print(candidate)
            candidate = nums[i]
        return candidate

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
        
#         nums.sort() 
#         return nums[len(nums)//2]

        # count = 0
        # candidate = None

        # for num in nums:
        #     if count == 0:
        #         candidate = num
        #     count += 1 if num == candidate else -1

        # return candidate

        # count = 0
        # majority_count = 0
        # majority = 0
        # visited = []
        # for i in range(len(nums)):
        #     count = 0
        #     if nums[i] not in visited:
        #         for j in range(len(nums)):
        #             if nums[j] == nums[i]:
        #                 count+=1
        #         visited.append(nums[i])
        #     if count > majority_count:
        #         majority_count = count
        #         majority = nums[i]    
        # return majority


       