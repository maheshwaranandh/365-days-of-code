class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        st=""
        for i in words:
            st+=i[0]
        return s==st
