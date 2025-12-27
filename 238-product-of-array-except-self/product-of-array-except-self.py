class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        answer = [1] * n

        # Prefix product
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Suffix product
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer

        # Using division
        # product_list = []
        # sum = 1
        # for j in range(1,len(nums)):
        #     sum = sum * nums[j]

        # product_list.append(sum)
        
        # for i in range(1,len(nums)):
        #     if nums[i] == 0:
        #         sum = 1
        #         for j in range(len(nums)):
        #             if i != j:
        #                sum = sum * nums[j] 
        #         product_list.append(sum)
        #     else:
        #         if product_list[i-1] ==0:
        #             sum = 0
        #         else:
        #             sum = int((product_list[i-1] / nums[i]) * nums[i-1])
        #         product_list.append(sum)

        # return product_list
