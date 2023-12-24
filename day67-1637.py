class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        l=[]
        for i in points:
            l.append(i[0])
        l=sorted(l)
        d=0
        for i in range(1,len(l)):
            d=max(d,l[i]-l[i-1])

        return d
            
        
