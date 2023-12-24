class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        d={}
        ans=[]
        f=0
        for i in arr:
            d[i]=d.get(i,0)+1
        for i in d:
            if i==d.get(i):
                ans.append(i)
                f=1
        if f==1:
            return max(ans)
        else:
            return -1
