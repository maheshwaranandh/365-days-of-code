class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        for i in sorted(nums1):
            if i in nums2:
                return i
        return min(min(nums1),min(nums2))*10+max(min(nums1),min(nums2))
