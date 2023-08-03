class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l=min(len(word1),len(word2))
        s=""
        l1=0
        l2=0
        for i in range(l):
            s+=word1[i]
            s+=word2[i]
            
        return s+word1[i+1:]+word2[i+1:]
