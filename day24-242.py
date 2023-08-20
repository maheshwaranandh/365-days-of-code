class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        maxl=0
        d={}
        for r in range(len(s)):
            d[s[r]]=d.get(s[r],0)+1

            while (r-l+1)-max(d.values())>k:
                d[s[l]]-=1
                l+=1
            maxl=max(maxl,r-l+1)
        return maxl
