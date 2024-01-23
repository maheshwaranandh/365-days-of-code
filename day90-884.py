class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ans=[]
        d1={}
        d2={}
        s1=list(map(str,s1.split()))
        s2=list(map(str,s2.split()))
        for i in s1:
            d1[i]=d1.get(i,0)+1
        for i in s2:
            d2[i]=d2.get(i,0)+1
        for i in d1:
            if d1[i]==1 and i not in d2:
                ans.append(i)
        for i in d2:
            if d2[i]==1 and i not in d1:
                ans.append(i)
        return ans
