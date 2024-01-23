class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vow="AEIOUaeiou"
        a=0
        b=0
        for i in range(len(s)):
            if i>=len(s)//2:
                if s[i] in vow:
                    b+=1
            else:
                if s[i] in vow:
                    a+=1
        return True if a==b else False
