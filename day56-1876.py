class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        l=0
        c=0
        r=3
        while(r<=len(s)):
            if len(s[l:r])==len(set(s[l:r])):
                c+=1
            l+=1
            r+=1
        return c
