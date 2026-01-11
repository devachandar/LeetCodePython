class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

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
        nums = set(nums)
        max_count = 0
        for num in nums:
            if num-1 not in nums:
                temp = num+1
                count = 1
                while temp in nums:
                    count+=1
                    temp+=1
                max_count = max(max_count,count)
        
        return max_count


