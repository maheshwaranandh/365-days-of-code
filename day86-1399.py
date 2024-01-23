class Solution:
    def countLargestGroup(self, n: int) -> int:
        d={}
        m=0
        for i in range(1,n+1):
            s=0
            for j in str(i):
                s+=int(j)
            d[s]=d.get(s,0)+1
            if max(d.values())>m:
                m=max(d.values())
                c=1
            elif d[s]==m:
                c+=1
        print(d)
        return c
        
