class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        result = []
        freq = Counter(nums)
        print(freq)
        for val in freq:
            if freq[val] > int(len(nums)/3):
                result.append(val)
            # print(freq[val])
        # result = []
        # for num in nums:
        #     if num not in result:
        #         if nums.count(num) > int(len(nums)/3):
        #             result.append(num)

        return result
