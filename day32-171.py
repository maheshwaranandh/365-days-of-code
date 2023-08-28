class Solution:
    def titleToNumber(self, s: str) -> int:
        m=1
        res=0
        for i in range(len(s)-1,-1,-1):
            res+=(ord(s[i])-ord("A")+1)*m
            m*=26
        return res
