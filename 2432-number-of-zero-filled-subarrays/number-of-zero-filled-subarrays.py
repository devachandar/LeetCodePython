class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        count = 0 
        result = 0

        for num in nums:
            if num == 0:
                count += 1
                result += count
            else:
                count = 0

        return result
        
        # count = 0   
        # sub_count = 0

        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         sub_count +=1
        #     else:
        #         if sub_count != 0:
        #             count = count + int(((sub_count)*(sub_count+1))/2)
        #             print("count",count)
        #             sub_count = 0
        # if sub_count != 0:
        #     count = count + int(((sub_count)*(sub_count+1))/2)
        # return count
                

        # sum_subarray = 0

        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         sum_subarray+=1
        #         for j in range(i+1,len(nums)):
        #             if nums[j] != 0:
        #                 break
        #             else:
        #                 sum_subarray+=1
        
        # return sum_subarray