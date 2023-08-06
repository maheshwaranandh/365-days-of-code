class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        
        l=[]

        for i in range(ord(s[0])-ord("A"),ord(s[3])-ord("A")+1):

            for j in range(int(s[1]),int(s[4])+1):

                l.append(chr(i+ord("A"))+str(j))

        return l
