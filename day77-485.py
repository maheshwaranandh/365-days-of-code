class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        m=0
        l=0
        r=0
        while(r<len(nums)):
            if nums[r]==1:
                c+=1
                r+=1
                m=max(m,c)
            else:
                c=0
                r+=1
                l=r
            
        return m
