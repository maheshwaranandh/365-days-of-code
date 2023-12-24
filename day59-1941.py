class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        k=d[s[0]]
        for i in d:
            if d[i]!=k:
                return False
        return True        
