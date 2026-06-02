class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # for i in range(len(nums)-1):
        #     for j in range(len(nums)):
        #         if nums[i] == nums[j] and abs(i-j) <=k:
        #             return True

        # return False



















        last_seen = {}

        for i, num in enumerate(nums):
            if num in last_seen:
                if i - last_seen[num] <= k:
                    return True
            last_seen[num] = i

        return False