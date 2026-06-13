class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count = 0
        prefix_sum = 0

        freq = defaultdict(int)
        freq[0] = 1

        for num in nums:
            prefix_sum += num

            count += freq[prefix_sum - k]

            freq[prefix_sum] += 1

        return count
        # count = 0
        
        # for i in range(len(nums)):
        #     sub_array = nums[i:]

        #     prefix = [0] * len(sub_array)

        #     for j in range(len(sub_array)):
        #         prefix[j] = prefix[j-1] + sub_array[j]

        #         if prefix[j] == k:
        #             count+=1
                    

        # return count