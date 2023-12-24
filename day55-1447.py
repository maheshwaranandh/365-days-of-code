class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        l=[]
        def gcd(a,b):
            while b>0:
                a,b=b,a%b
            return a
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                if gcd(i,j)==1 :
                    l.append(str(i)+"/"+str(j))
        return l
