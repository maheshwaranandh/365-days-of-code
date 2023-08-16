class Solution:
    def countAsterisks(self, s: str) -> int:
        c=0
        cs=0
        for i in s:
            if i=="|":
                c+=1
            elif c%2==0:
                if i=="*":
                    cs+=1
        return cs
