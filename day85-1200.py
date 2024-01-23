class Solution:
    def minimumAbsDifference(self, nums: List[int]) -> List[List[int]]:
        ab=float('inf')
        nums=sorted(nums)
        for i in range(len(nums)-1):
            j=i+1
            if abs(nums[i]-nums[j])<ab:
                ab=abs(nums[i]-nums[j])
                l=[]
            if abs(nums[i]-nums[j])==ab:
                l.append([nums[i],nums[j]])
        return l
