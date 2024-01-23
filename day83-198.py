class Solution:
    def rob(self, nums: List[int]) -> int:
        prev=0
        cur=0
        for i in range(len(nums)):
            temp=max(prev+nums[i],cur)
            prev=cur
            cur=temp
        return cur
