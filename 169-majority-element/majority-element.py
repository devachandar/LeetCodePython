class Solution:
    def majorityElement(self, nums: List[int]) -> int:
    
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate

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


        # freq = []
        # for i in range(len(nums)):
        #     count = 0
        #     if nums[i] not in freq:
        #         for j in range(len(nums)):
        #             if nums[j] == nums[i]:
        #                 count+=1
            
        #         freq[nums[i]]=count
        # print("freq",freq)