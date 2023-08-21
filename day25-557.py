class Solution:
    def reverseWords(self, s: str) -> str:
        
        l=list(map(str,s.split()))
        s=""
        for i in l:
            s+=i[::-1]+" "
        return s[0:len(s)-1]
