class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []

        # print(result+[2]*3)

        freq_nums1 = Counter(nums1)
        freq_nums2 = Counter(nums2)

        for val in freq_nums1:
            min_val = min(freq_nums1[val], freq_nums2[val])
            if min_val >0:
                result+=[val]*min_val

        return result
