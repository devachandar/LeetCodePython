class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        left_max = 0
        right_max = 0

        water = 0

        while left < right:

            if height[left] < height[right]:

                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]

                left += 1

            else:

                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]

                right -= 1

        return water


        
        # if len(height) <= 2:
        #     return 0

        # left = 0
        # right = 1
        # idx_middle = 1
        # total_count = 0
        # middle_count = 0

        # def find_count(left,right):
        #     count = 0
        #     sub_height = height[left+1:right]
        #     min_height = min(height[left],height[right])
        #     for ht in sub_height:
        #         count += abs(min_height - ht)

        #     return count

        # while right < len(height):
        #     print(left,right,idx_middle)
        #     if height[right]> height[left]:
        #         print("sending right", left,right)

        #         total_count += find_count(left,right)
        #         print("total",total_count)
        #         left = right
        
        #         right = right + 1
        #         middle_count = 0
        #         idx_middle = right
                
                

        #     elif height[right] >= height[idx_middle] and idx_middle!= right:
        #         print("sending middle", left,right)
        #         middle_count = find_count (left, right)
        #         print("middle_count", middle_count)
        #         idx_middle = right
        #         right+=1

        #     else:
        #         right +=1

        # if middle_count:
        #     total_count +=middle_count

        # return total_count

          

                    