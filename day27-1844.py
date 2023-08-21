class Solution:
    def replaceDigits(self, s: str) -> str:
        for i in range(len(s)):
            if not s[i].isalpha():
                s=s.replace(s[i],chr(ord(s[i-1])+int(s[i])),1)
        return s
