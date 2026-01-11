class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        need = defaultdict(int)

        for num in nums:
            if freq[num] == 0:
                continue

            # Case 1: extend an existing subsequence
            if need[num] > 0:
                need[num] -= 1
                need[num + 1] += 1

            # Case 2: start a new subsequence
            elif freq[num + 1] > 0 and freq[num + 2] > 0:
                freq[num + 1] -= 1
                freq[num + 2] -= 1
                need[num + 3] += 1

            # Case 3: impossible
            else:
                return False

            freq[num] -= 1

        return True
