class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        # result = [-1] * len(nums2)
        result = {}

        for num in nums2:

            while stack and num > stack[-1]:
                idx = stack.pop()
                result[idx] = num


            stack.append(num)

        print(result)
        return [ result[num] if num in result else -1 for num in nums1 ]