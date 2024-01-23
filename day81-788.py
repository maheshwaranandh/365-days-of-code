class Solution:
    def rotatedDigits(self, n: int) -> int:
        c=0
        for i in range(1,n+1):
            s=""
            f=0
            for j in str(i):
                if j=="0" or j=="1" or j=="8":
                    s+=j
                elif j=="2":
                    s+="5"
                elif j=="5":
                    s+="2"
                elif j=="6":
                    s+="9"
                elif j=="9":
                    s+="6"
                else:
                    f=1
                    break
            if f==0 and int(s)!=i:
                c+=1    
        return c
