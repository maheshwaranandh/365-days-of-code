class Solution:
    def trap(self, height: List[int]) -> int:
        lmax=0
        rmax=0
        water=0
        maxl=[0]*len(height)
        maxr=[0]*len(height)
        for i in range(len(height)):
            maxl[i]=lmax
            if height[i]>lmax:
                lmax=height[i]
        for i in range(len(height)-1,-1,-1):
            maxr[i]=rmax
            if height[i]>rmax:
                rmax=height[i]
        for i in range(len(height)):
            w=min(maxl[i],maxr[i])-height[i]
            if w>0:
                water+=w
        return water
