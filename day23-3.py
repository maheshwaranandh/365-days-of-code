class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        hs=set()
        maxl=0
        
        for r in range(len(s)):
            while s[r] in hs:
                hs.remove(s[l])
                l+=1
            hs.add(s[r])
            maxl=max(maxl,r-l+1)
        return maxl
