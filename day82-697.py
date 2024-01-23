class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d={}
        d1={}
        x=0
        deg=0

        for i,a in enumerate(nums):
            d.setdefault(a,i)
            d1[a]=d1.get(a,0)+1
            if d1[a]>deg:
                deg=d1[a]
                x=i-d[a]+1
            elif d1[a]==deg:
                x=min(x,i-d[a]+1)
        return x
