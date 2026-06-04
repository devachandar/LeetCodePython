class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) <= 0:
            return 0

        num_set = sorted(set(nums))

        max_count = 1
        count = 1
        if len(num_set) == 1:
            return 1
        
        for i in range(1,len(num_set)):
            if num_set[i]-1 == num_set[i-1]:
                count+=1
                max_count = max(max_count,count)
            else:
                count = 1

        return max_count
        

        # num_set = set(nums)
        # longest = 0

        # for num in num_set:
        #     # only start counting if num is the start of a sequence
        #     if num - 1 not in num_set:
        #         current = num
        #         length = 1

        #         while current + 1 in num_set:
        #             current += 1
        #             length += 1

        #         longest = max(longest, length)

        # return longest
        # nums = set(nums)
        # max_count = 0
        # for num in nums:
        #     if num-1 not in nums:
        #         temp = num+1
        #         count = 1
        #         while temp in nums:
        #             count+=1
        #             temp+=1
        #         max_count = max(max_count,count)
        
        # return max_count


