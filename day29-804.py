class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        giv=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        arr=[]
        for i in words:
            s=""
            for j in i:
                s+=giv[ord(j)-ord("a")]
            if s not in arr:
                arr.append(s)
        return len(arr)
