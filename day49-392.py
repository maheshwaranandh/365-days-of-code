class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ls=len(s)
        lt=len(t)
        i=0
        j=0
        while(True):
            if i==ls:
                return True
            if j==lt:
                return False
            if t[j]==s[i]:
                i+=1
                j+=1
            else:
                j+=1
            
