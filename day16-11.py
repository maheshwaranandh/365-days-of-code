class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxx=0
        i=0
        j=len(height)-1
        while(i<j):
            area=(j-i)*min(height[i],height[j])
            if height[i]>height[j]:
                j-=1
            elif height[j]>=height[i]:
                i+=1
            maxx=max(maxx,area)
        return maxx
      
