class Solution:
    def finalString(self, s: str) -> str:
        k=""
        for i,x in enumerate(s):
            if x=="i":
                k=k[::-1]
            else:
                k+=x
            
        return k
