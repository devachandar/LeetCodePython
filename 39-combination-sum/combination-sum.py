from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # result = []
        # for i in range(len(candidates)):
        #     target_found = []
        #     if candidates[i] == target:
        #         target_found.append(candidates[i])
        #         result.append(target_found.copy())
        #     elif (candidates[i] < target):
        #         if target % candidates[i] == 0:
        #             target_found.append(candidates[i]) 
        #             target_found *= target//candidates[i]
        #             result.append(target_found.copy())
        #         # check_list = []
        #         # check_list.append(candidates[i])
        #         for k in range(i+1,len(candidates)):
        #             check_list = []
        #             check_list.append(candidates[i])
        #             for j in range(k,len(candidates)):
        #                 print("before",result)
        #                 check_list.append(candidates[j])
        #                 print("for",check_list)
        #                 total = sum(check_list)
        #                 if total <= target:
        #                     rem = target % total
        #                     print(rem)
        #                     if rem == 0:
        #                         result.append(check_list.copy())
        #                     else:
        #                         factors = [x for x in check_list if rem % x == 0 ]
        #                         for factor in factors:
        #                             rep_val = (target - total) // rem
        #                             print("rep_val",rep_val) 
        #                             temp_list = check_list.copy() 
        #                             temp_list.extend([factor] * rep_val)
        #                             print("check_list",temp_list)
        #                             if sum(temp_list) == target:
        #                                 result.append(temp_list.copy())
        #                                 print("else",result)
        # return result
        
        result = []

        def backtrack(start, path, total):
            # If current total equals target, we found a valid combination
            if total == target:
                result.append(path.copy())
                return
            # If total exceeds target, no need to continue
            if total > target:
                return

            # Try each candidate starting from 'start'
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                # Allow the same number to be used again by passing 'i'
                backtrack(i, path, total + candidates[i])
                path.pop()  # Backtrack

        backtrack(0, [], 0)
        return result
