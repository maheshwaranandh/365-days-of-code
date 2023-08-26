class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        templ=sorted(nums)
        d={}
        l=[]
        for i,x in enumerate(templ):
            if x not in d:
                d[x]=i
        for i in nums:
            l.append(d[i])
        return l
