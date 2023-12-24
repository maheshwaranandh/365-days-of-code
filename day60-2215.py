class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        l=[]
        l1=[]
        l2=list(set(nums2))
        for i in set(nums1):
            if i not in nums2:
                l1.append(i)
            else:
                l2.remove(i)

        return [l1,l2]
