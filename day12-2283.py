class Solution:
    def digitCount(self, s: str) -> bool:
        c=0
        l=[]
        for i in s:
            l.append(int(i))
        for  i in l:
            if(l.count(c)!=i):
                return False
            c+=1
        return True
            
