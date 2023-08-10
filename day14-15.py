class Solution:
    def threeSum(self, s: List[int]) -> List[List[int]]:
        s.sort()
        ans=[]
        for i in range(len(s)):
            if i!=0 and s[i]==s[i-1]:
                continue
            l=i+1
            r=len(s)-1
            while(l<r):
                if s[i]+s[l]+s[r]==0:
                    ans.append([s[i],s[l],s[r]])
                    l+=1
                    while s[l]==s[l-1] and l<r:
                        l+=1
                elif s[i]+s[l]+s[r]<0:
                    l+=1
                elif s[i]+s[l]+s[r]>0:
                    r-=1
            
        return ans
