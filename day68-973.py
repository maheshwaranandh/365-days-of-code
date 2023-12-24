class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dic={}
        for i in range(len(points)):
            d=((points[i][0])**2+(points[i][1])**2)**(1/2)
            dic[i]=d
        kl=list(sorted(dic,key=dic.get))
        ans=[]
        for i in range(k):
            ans.append(points[kl[i]])
        return ans
        
