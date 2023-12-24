class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l=0
        r=len(s)
        sm=0
        c=0
        while(l<r):
            if s[l]=="R":
                sm+=1
            else:
                sm-=1
            if sm==0:
                c+=1
                sm=0
            l+=1
        return c
