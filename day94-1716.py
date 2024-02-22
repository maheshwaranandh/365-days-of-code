class Solution:
    def totalMoney(self, n: int) -> int:
        m=1
        tot=0
        for i in range(n):
            if i%7==0:
                z=m
                m+=1
            tot+=z
            z+=1
        return tot
