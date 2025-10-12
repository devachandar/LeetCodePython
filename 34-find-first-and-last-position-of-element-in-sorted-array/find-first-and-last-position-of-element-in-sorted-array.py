class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        try:
            index_list = [-1,-1]
            first_index = nums.index(target)
            index_list[0] = first_index
            index_list[1] = first_index
            j = first_index+1

            while j<len(nums):
                if nums[j]==target:
                    index_list[1]=j
                j+=1

            return index_list
            
        except:
            return [-1,-1]