class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) -  1

        while left < right:
            curr_sum = numbers[left] + numbers[right]

            if curr_sum == target:
                return [left+1,right+1]
            elif curr_sum > target:
                right-=1
            else:
                left+=1

        # output = []
        # for i in range(len(numbers)):
        #     for j in range(i+1,len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             output.append(i+1)
        #             output.append(j+1)
        #             return output
        #         if numbers[i] + numbers[j] > target:
        #             break